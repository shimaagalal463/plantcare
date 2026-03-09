#!/usr/bin/env python3
from plantcare.storage import Book
from plantcare.search import search_care_logs
import sys

def main():
    book = Book.load(sys.argv[1])
    q = sys.argv[2] if len(sys.argv) > 2 else ""
    for hit in search_care_logs(book, q):
        print(hit)

if __name__ == "__main__":
    main()
