#!/usr/bin/env python3

import typer
from . import fasta

app = typer.Typer()
app.add_typer(fasta.app, name="fasta")

def main():
    app()

if __name__ == "__main__":
    app()