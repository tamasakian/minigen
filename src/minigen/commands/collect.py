#!/usr/bin/env python3

import typer

app = typer.Typer(help="collect tools")

@app.command("blast-to-homology-table")
def blast_to_homology_table(
    input_file: str = typer.Argument(..., help="path to input file with blast results"),
    output_file: str = typer.Argument(..., help="path to output file for homology table"),
):
    from minigen.io.blast import parse_blast
    from minigen.core.blast import to_homology_table
    from minigen.io.homology_table import write_homology_table
    records = parse_blast(input_file)
    homology_records = to_homology_table(records)
    write_homology_table(output_file, homology_records)