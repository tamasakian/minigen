#!/usr/bin/env python3

import typer
from minigen.io.text import write_text

app = typer.Typer(help="identify tools")

@app.command("ensembl-canonical")
def ensembl_canonical(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import identify_canonical
    records = parse_gff3(input_file)
    canonical_ids = identify_canonical(records)
    write_text(output_file, canonical_ids)