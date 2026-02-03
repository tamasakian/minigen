#!/usr/bin/env python3

import typer

app = typer.Typer(help="generate tools")

@app.command("bed6-upstream")
def bed6_upstream(
    input_file: str = typer.Argument(..., help="path to input bed6 file"),
    output_file: str = typer.Argument(..., help="path to output bed6 file for upstream"),
    bp: str = typer.Argument(..., help="number of base pairs upstream to extract"),
):
    from minigen.io.bed6 import parse_bed6, write_bed6
    from minigen.core.bed6 import generate_upstream
    records = parse_bed6(input_file)
    upstream_records = generate_upstream(records, int(bp))
    write_bed6(output_file, upstream_records)

@app.command("fasta-upstream")
def fasta_upstream(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file for upstream sequences"),
    bed6_file: str = typer.Argument(..., help="path to bed6 file with feature coordinates"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.io.bed6 import parse_bed6
    from minigen.core.fasta import generate_upstream
    fasta_records = parse_fasta(input_file)
    bed6_records = parse_bed6(bed6_file)
    upstream_records = generate_upstream(fasta_records, bed6_records)
    write_fasta(output_file, upstream_records)