#!/usr/bin/env python3

import typer
from .commands import collect, detect, extract, identify, tag, transform

app = typer.Typer(help="a minimal genome analysis toolkit")

app.add_typer(collect.app, name="collect")
app.add_typer(detect.app, name="detect")
app.add_typer(extract.app, name="extract")
app.add_typer(identify.app, name="identify")
app.add_typer(tag.app, name="tag")
app.add_typer(transform.app, name="transform")

def main():
    app()

if __name__ == "__main__":
    main()
