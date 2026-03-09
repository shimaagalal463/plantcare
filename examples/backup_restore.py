#!/usr/bin/env python3
import sys
from pathlib import Path
from plantcare.backup import create_backup, restore_backup

def main():
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    create_backup(src, dest)
    print("backup written to %s" % dest)

if __name__ == "__main__":
    main()
