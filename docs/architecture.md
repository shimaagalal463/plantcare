# Architecture

plantcare is a stdlib-first CLI. One JSON file (`Book`) holds plants, rooms,
care logs, watering schedules, pots, fertilizers, sessions, notes, goals, tags,
collections, and an audit log.

## Why JSON not SQLite

I wanted `grep`, `jq`, and rsync without binary blobs. Migrations are explicit
Python functions in `migrate.py`.

## Module map

| Area | Modules |
|------|---------|
| Models | plant, room, watering, schedule, care_log, session, note, pot, fertilizer, goal |
| Storage | storage, migrate, backup |
| I/O | io_csv, io_json, io_excel, io_plantly, io_blossom, io_gardenpad |
| Logic | catalog, reports, stats, search, timeline, collections, tags_manager |
| Infra | errors, parser, validators, light_level, soil, humidity, season, plugins, audit_log, server, cli |

Schema versions: 0 (proto) → 1 (published) → 2 (schedules/pots) → 3 (collections/fertilizer).
