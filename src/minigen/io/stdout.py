#!/usr/bin/env python3

from pathlib import Path

def print_filename(path: str) -> None:
    name = Path(path).name
    print(name.rsplit(".", 1)[0])