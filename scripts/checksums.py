"""Print SHA-256 and byte counts for real data files. Standard library only."""
from pathlib import Path
import csv
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
writer = csv.writer(sys.stdout)
writer.writerow(["relative_path", "bytes", "sha256"])
for folder in ("raw", "processed", "splits"):
    for path in sorted((root / "data" / folder).rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        writer.writerow([path.relative_to(root).as_posix(), path.stat().st_size, digest.hexdigest()])
