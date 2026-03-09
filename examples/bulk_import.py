#!/usr/bin/env python3
"""Import CSV care logs into a plantcare journal."""
import sys
from pathlib import Path
from plantcare.storage import init_book, Book
from plantcare.io_csv import import_care_logs_csv

def main():
    if len(sys.argv) < 3:
        print("usage: bulk_import.py JOURNAL.json care_logs.csv")
        sys.exit(1)
    journal, csv_path = Path(sys.argv[1]), Path(sys.argv[2])
    if journal.exists():
        book = Book.load(journal)
    else:
        book = init_book(journal)
    n = import_care_logs_csv(book, csv_path)
    book.save()
    print("imported %d rows" % n)

if __name__ == "__main__":
    main()
