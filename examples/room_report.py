#!/usr/bin/env python3
"""Print a room summary from an existing plantcare journal."""
import sys
from plantcare.storage import Book
from plantcare.reports import room_report

def main():
    if len(sys.argv) < 2:
        print("usage: room_report.py JOURNAL.json [room_id]")
        sys.exit(1)
    book = Book.load(sys.argv[1])
    rid = int(sys.argv[2]) if len(sys.argv) > 2 else (book.rooms[0].id if book.rooms else 0)
    print(room_report(book, rid))

if __name__ == "__main__":
    main()
