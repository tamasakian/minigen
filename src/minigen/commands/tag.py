#!/usr/bin/env python3

import typer

app = typer.Typer(help="tag tools")

@app.command("fasta")
def fasta(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file"),
    tag: str = typer.Argument(..., help="tag to add to fasta headers"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.core.fasta import tag_fasta
    records = parse_fasta(input_file)
    new_records = tag_fasta(records, tag)
    write_fasta(output_file, new_records)

@app.command("mcscanx-bed4-name")
def mcscanx_bed4_name(
    input_file: str = typer.Argument(..., help="path to input mcscanx bed4 file"),
    output_file: str = typer.Argument(..., help="path to output mcscanx bed4 file"),
    tag: str = typer.Argument(..., help="tag to add to bed4 names"),
):
    from minigen.io.mcscanx_bed4 import parse_mcscanx_bed4, write_mcscanx_bed4
    from minigen.core.mcscanx_bed4 import tag_mcscanx_bed4_name
    records = parse_mcscanx_bed4(input_file)
    new_records = tag_mcscanx_bed4_name(records, tag)
    write_mcscanx_bed4(output_file, new_records)