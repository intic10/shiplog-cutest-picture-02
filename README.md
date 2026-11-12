# Cutest picture entry

`main.py` copies the bytes of `art.jpg` to `/output/entry.png`. The copy is exact: the program reads and writes the file in binary mode and does not decode or re-encode the image. The output path ends in `.png` because the contest requires that filename; the file contents stay the original JPEG bytes.

The program uses only the Python standard library. It does not use the network or third-party packages.

## Run

```bash
python main.py
```

The program creates `/output` when that directory is missing, then writes `/output/entry.png`.
