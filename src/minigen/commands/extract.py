#!/usr/bin/env python3

import typer
from minigen.io.text import parse_text

app = typer.Typer(help="extract tools")

@app.command("fasta")
def fasta(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.core.fasta import extract_fasta
    records = parse_fasta(input_file)
    filters = parse_text(text_file)
    new_records = extract_fasta(records, filters)
    write_fasta(output_file, new_records)

@app.command("gff3-seqid")
def gff3_seqid(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output gff3 file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
):
    from minigen.io.gff3 import parse_gff3, write_gff3
    from minigen.core.gff3 import extract_gff3_by_seqid
    records = parse_gff3(input_file)
    filters = parse_text(text_file)
    new_records = extract_gff3_by_seqid(records, filters)
    write_gff3(output_file, new_records)

@app.command("gff3-type")
def gff3_type(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output gff3 file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
):
    from minigen.io.gff3 import parse_gff3, write_gff3
    from minigen.core.gff3 import extract_gff3_by_type
    records = parse_gff3(input_file)
    filters = parse_text(text_file)
    new_records = extract_gff3_by_type(records, filters)
    write_gff3(output_file, new_records)

@app.command("gff3-attributes")
def gff3_attributes(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output gff3 file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
    attr_key: str = typer.Argument(..., help="attribute key for extracting (e.g., ID, transcript_id, protein_id)"),
):
    from minigen.io.gff3 import parse_gff3, write_gff3
    from minigen.core.gff3 import extract_gff3_by_attributes
    records = parse_gff3(input_file)
    filters = parse_text(text_file)
    new_records = extract_gff3_by_attributes(records, filters, attr_key)
    write_gff3(output_file, new_records)

@app.command("mcscanx-bed4-chrom")
def mcscanx_bed4_chrom(
    input_file: str = typer.Argument(..., help="path to input mcscanx bed4 file"),
    output_file: str = typer.Argument(..., help="path to output mcscanx bed4 file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
):
    from minigen.io.mcscanx_bed4 import parse_mcscanx_bed4, write_mcscanx_bed4
    from minigen.core.mcscanx_bed4 import extract_mcscanx_bed4_by_chrom
    records = parse_mcscanx_bed4(input_file)
    filters = parse_text(text_file)
    new_records = extract_mcscanx_bed4_by_chrom(records, filters)
    write_mcscanx_bed4(output_file, new_records)

@app.command("mcscanx-bed4-name")
def mcscanx_bed4_name(
    input_file: str = typer.Argument(..., help="path to input mcscanx bed4 file"),
    output_file: str = typer.Argument(..., help="path to output mcscanx bed4 file"),
    text_file: str = typer.Argument(..., help="path to text file with ids to extract"),
):
    from minigen.io.mcscanx_bed4 import parse_mcscanx_bed4, write_mcscanx_bed4
    from minigen.core.mcscanx_bed4 import extract_mcscanx_bed4_by_name
    records = parse_mcscanx_bed4(input_file)
    filters = parse_text(text_file)
    new_records = extract_mcscanx_bed4_by_name(records, filters)
    write_mcscanx_bed4(output_file, new_records)
