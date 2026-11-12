"""Copy the contest artwork bytes to the required output path."""

import pathlib
import shutil


def main() -> None:
    source = pathlib.Path(__file__).resolve().parent / "art.jpg"
    destination = pathlib.Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
