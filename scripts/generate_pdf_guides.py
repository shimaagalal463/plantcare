#!/usr/bin/env python3
"""Minimal PDF trail permit stubs for fixture bulk."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "fixtures" / "guides"


def minimal_pdf(text: str) -> bytes:
    content = f"BT /F1 12 Tf 50 750 Td ({text}) Tj ET"
    objs = []
    objs.append(b"1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj\n")
    objs.append(b"2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj\n")
    objs.append(
        b"3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 4 0 R /Resources<< /Font<< /F1 5 0 R >> >> >>endobj\n"
    )
    stream = content.encode("latin-1", errors="replace")
    objs.append(f"4 0 obj<< /Length {len(stream)} >>stream\n".encode() + stream + b"\nendstream endobj\n")
    objs.append(b"5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>endobj\n")
    body = b"".join(objs)
    xref_pos = len(b"%PDF-1.4\n") + len(body)
    trailer = f"xref\n0 6\n0000000000 65535 f \n".encode()
    # simplified — good enough for bytes in zip
    return b"%PDF-1.4\n" + body + trailer + b"trailer<< /Size 6 /Root 1 0 R >>startxref\n" + str(xref_pos).encode() + b"\n%%EOF\n"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for i in range(40):
        (OUT / f"guide_{i:03d}.pdf").write_bytes(minimal_pdf(f"Care guide #{i}"))
    print("wrote PDF guide fixtures")

if __name__ == "__main__":
    main()
