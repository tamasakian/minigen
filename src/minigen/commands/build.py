#!/usr/bin/env python3

import typer

app = typer.Typer(help="build tools")

@app.command("fasta-homologs")
def fasta_homologs(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_dir: str = typer.Argument(..., help="path to output directory for homolog fasta files"),
    homologs_file: str = typer.Argument(..., help="path to homologs file"),
):
    from minigen.io.fasta import parse_fasta, build_fasta_by_homologs
    from minigen.io.homologs import parse_homologs
    records = parse_fasta(input_file)
    homologs = parse_homologs(homologs_file)
    build_fasta_by_homologs(output_dir, records, homologs)