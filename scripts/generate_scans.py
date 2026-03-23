#!/usr/bin/env python3
"""Generate noise PNG field attachments (zlib — uncompressible)."""
import random
import zlib
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "fixtures" / "attachments"

def _chunk(name, data):
    import struct, zlib as z
    crc = z.crc32(name + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + name + data + struct.pack(">I", crc)

def fake_png(width=48, height=48, seed=0):
    rng = random.Random(seed)
    out = bytearray(PNG_SIGNATURE)
    ihdr = width.to_bytes(4, "big") + height.to_bytes(4, "big") + b"\x08\x02\x00\x00\x00"
    out += _chunk(b"IHDR", ihdr)
    rows = bytearray()
    for _ in range(height):
        rows.append(0)
        rows.extend(rng.randbytes(width * 3))
    out += _chunk(b"IDAT", zlib.compress(bytes(rows), 1))
    out += _chunk(b"IEND", b"")
    return bytes(out)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for i in range(1000):
        (OUT / f"scan_{i:05d}.png").write_bytes(fake_png(width=56, height=56, seed=i))
    print("wrote 1000 PNG attachments")

if __name__ == "__main__":
    main()
