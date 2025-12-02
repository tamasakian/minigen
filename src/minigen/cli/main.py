#!/usr/bin/env python3

import typer
from . import ensembl, fasta, mcscanx

app = typer.Typer()
app.add_typer(ensembl.app, name="ensembl")
app.add_typer(fasta.app, name="fasta")
app.add_typer(mcscanx.app, name="mcscanx")

def main():
    app()

if __name__ == "__main__":
    app()