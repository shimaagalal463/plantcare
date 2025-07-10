"""plantcare CLI."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .backup import create_backup
from .care_log import CareLog
from .io_csv import export_care_logs_csv, import_care_logs_csv
from .io_plantly import import_plantly_csv
from .migrate import CURRENT_SCHEMA, migration_plan
from .plant import Plant
from .reports import room_report, summary_report
from .room import Room
from .stats import action_counts
from .storage import Book, init_book


# TODO: config file for default journal path instead of env var only

def _default_journal() -> Path:
    return Path.home() / "plantcare.json"


def cmd_init(args: argparse.Namespace) -> int:
    path = Path(args.path)
    init_book(path)
    print("initialized %s (schema %d)" % (path, CURRENT_SCHEMA))
    return 0


def cmd_room_add(args: argparse.Namespace) -> int:
    book = Book.load(args.journal)
    room = Room(name=args.name, light_level=args.light or "medium", humidity=args.humidity or "medium")
    book.add_room(room)
    book.save()
    print("room #%d" % room.id)
    return 0


def cmd_plant_add(args: argparse.Namespace) -> int:
    book = Book.load(args.journal)
    plant = Plant(name=args.name, species=args.species or "", room_id=args.room, acquired_date=args.date or "")
    book.add_plant(plant)
    book.save()
    print("plant #%d" % plant.id)
    return 0


def cmd_care_add(args: argparse.Namespace) -> int:
    book = Book.load(args.journal)
    log = CareLog(
        plant_id=args.plant,
        action=args.action or "water",
        performed_at=args.at or (args.date + "T12:00:00"),
        notes=args.notes or "",
        soil_moisture=args.moisture or "",
    )
    book.add_care_log(log)
    book.save()
    print("care #%d" % log.id)
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    book = Book.load(args.journal)
    if args.kind == "summary":
        print(summary_report(book))
    elif args.kind == "room":
        print(room_report(book, args.id))
    else:
        for name, cnt in action_counts(book)[: args.top]:
            print("%s\t%d" % (name, cnt))
    return 0


def cmd_import(args: argparse.Namespace) -> int:
    book = Book.load(args.journal)
    path = Path(args.file)
    if args.format == "csv":
        n = import_care_logs_csv(book, path)
    elif args.format == "plantly":
        n = import_plantly_csv(book, path)
    else:
        print("unknown format", file=sys.stderr)
        return 1
    book.save()
    print("imported %d records" % n)
    return 0


def cmd_backup(args: argparse.Namespace) -> int:
    create_backup(args.journal, args.dest, label=args.label or "")
    print("backup -> %s" % args.dest)
    return 0


def cmd_migrate(args: argparse.Namespace) -> int:
    raw = __import__("json").loads(Path(args.journal).read_text(encoding="utf-8"))
    if args.check:
        print("needs migrations from: %s" % migration_plan(raw))
        return 0
    book = Book.load(args.journal)
    book.save()
    print("at schema %d" % book.schema_version)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="plantcare", description="Houseplant care tracker CLI")
    p.add_argument("--journal", "-j", default=str(_default_journal()))
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("init")
    s.add_argument("path")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("room")
    rsub = s.add_subparsers(dest="room_cmd")
    radd = rsub.add_parser("add")
    radd.add_argument("--name", required=True)
    radd.add_argument("--light")
    radd.add_argument("--humidity")
    radd.set_defaults(func=cmd_room_add)

    s = sub.add_parser("plant")
    psub = s.add_subparsers(dest="plant_cmd")
    padd = psub.add_parser("add")
    padd.add_argument("--name", required=True)
    padd.add_argument("--species")
    padd.add_argument("--room", type=int)
    padd.add_argument("--date")
    padd.set_defaults(func=cmd_plant_add)

    s = sub.add_parser("care")
    csub = s.add_subparsers(dest="care_cmd")
    cadd = csub.add_parser("add")
    cadd.add_argument("--plant", type=int, required=True)
    cadd.add_argument("--action", default="water")
    cadd.add_argument("--date", default="2025-01-01")
    cadd.add_argument("--at")
    cadd.add_argument("--notes")
    cadd.add_argument("--moisture")
    cadd.set_defaults(func=cmd_care_add)

    s = sub.add_parser("report")
    s.add_argument("kind", choices=["summary", "room", "actions"])
    s.add_argument("--id", type=int, default=1)
    s.add_argument("--top", type=int, default=10)
    s.set_defaults(func=cmd_report)

    s = sub.add_parser("import")
    s.add_argument("format", choices=["csv", "plantly"])
    s.add_argument("file")
    s.set_defaults(func=cmd_import)

    s = sub.add_parser("backup")
    s.add_argument("dest")
    s.add_argument("--label")
    s.set_defaults(func=cmd_backup)

    s = sub.add_parser("migrate")
    s.add_argument("--check", action="store_true")
    s.set_defaults(func=cmd_migrate)

    return p


def main(argv: list | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())


# --- extended cli helpers ---

def cli_transform_0(value, scale=1):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_1(value, scale=2):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_2(value, scale=3):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_3(value, scale=4):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_4(value, scale=5):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_5(value, scale=6):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_6(value, scale=7):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_7(value, scale=8):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_8(value, scale=9):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_9(value, scale=10):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_10(value, scale=11):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value

def cli_transform_11(value, scale=12):
    if value is None:
        return None
    if isinstance(value, str):
        return value.strip()[: scale * 8] or None
    if isinstance(value, (int, float)):
        return round(value * scale / (scale + 1), 4)
    if isinstance(value, list):
        return value[: scale]
    return value
