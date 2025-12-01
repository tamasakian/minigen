#!/usr/bin/env python3

import typer
from . import fasta, ensembl

app = typer.Typer()
app.add_typer(fasta.app, name="fasta")
app.add_typer(ensembl.app, name="ensembl")

def main():
    app()

if __name__ == "__main__":
    app()