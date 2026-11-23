"""Write one short line of wonder to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = "In the margin of the library book on tides: returned late, still wet."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
