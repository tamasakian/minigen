#!/usr/bin/env python3

import typer
from minigen.core.ensembl.io import parse_gff3, write_list
from minigen.core.ensembl.utils import query_canonical

app = typer.Typer()

@app.command("canonical-only")
def canonical_only(input_file: str, output_file: str) -> None:
    records = parse_gff3(input_file)
    canonical_list = query_canonical(records)
    write_list(output_file, canonical_list)