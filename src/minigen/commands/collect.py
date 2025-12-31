#!/usr/bin/env python3

import typer

app = typer.Typer(help="collect tools")

@app.command("blast-to-homologs")
def blast_to_homologs(
    input_file: str = typer.Argument(..., help="path to input file with blast results"),
    output_file: str = typer.Argument(..., help="path to output file for homologs"),
):
    from minigen.io.blast import parse_blast
    from minigen.core.blast import to_homologs
    from minigen.io.homologs import write_homologs
    records = parse_blast(input_file)
    homology_records = to_homologs(records)
    write_homologs(output_file, homology_records)