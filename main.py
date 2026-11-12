"""Copy contest artwork bytes to /output/entry.png.

Reads art.jpg in binary mode and writes those same bytes to the contest
output path. The file is not decoded or re-encoded, so the output is a
bit-for-bit copy of the JPEG (the .png suffix is required by the contest).
Uses only the Python standard library.
"""

import pathlib


def main() -> None:
    source = pathlib.Path(__file__).resolve().parent / "art.jpg"
    destination = pathlib.Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    artwork = source.read_bytes()
    destination.write_bytes(artwork)


if __name__ == "__main__":
    main()
