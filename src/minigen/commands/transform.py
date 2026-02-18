#!/usr/bin/env python3

import typer

app = typer.Typer(help="transform tools")

@app.command("gff3-to-text")
def gff3_to_text(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
    attr_key: str = typer.Argument(..., help="attribute key for text output (e.g., ID, transcript_id, protein_id)"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import to_text
    from minigen.io.text import write_text
    records = parse_gff3(input_file)
    ids = to_text(records, attr_key)
    write_text(output_file, ids)

@app.command("gff3-to-bed6")
def gff3_to_bed6(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output bed6 file"),
    attr_key: str = typer.Argument(..., help="attribute key for bed6 names (e.g., ID, transcript_id, protein_id)"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import to_bed6
    from minigen.io.bed6 import write_bed6
    records = parse_gff3(input_file)
    bed6_records = to_bed6(records, attr_key)
    write_bed6(output_file, bed6_records)

@app.command("gff3-to-bed4mcscanx")
def gff3_to_bed4mcscanx(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output mcscanx bed4 file"),
    attr_key: str = typer.Argument(..., help="attribute key for bed4 names (e.g., ID, transcript_id, protein_id)"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import to_bed4mcscanx
    from minigen.io.bed4mcscanx import write_bed4mcscanx
    records = parse_gff3(input_file)
    bed4_records = to_bed4mcscanx(records, attr_key)
    write_bed4mcscanx(output_file, bed4_records)

@app.command("blast-to-bed6")
def blast_to_bed6(
    input_file: str = typer.Argument(..., help="path to input blast file in outfmt 6"),
    output_file: str = typer.Argument(..., help="path to output bed6 file"),
):
    from minigen.io.blast import parse_blast
    from minigen.core.blast import to_bed6
    from minigen.io.bed6 import write_bed6
    blast_records = parse_blast(input_file)
    bed6_records = to_bed6(blast_records)
    write_bed6(output_file, bed6_records)

@app.command("bed6-to-fasta")
def bed6_to_fasta(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file for sequences"),
    bed6_file: str = typer.Argument(..., help="path to bed6 file with feature coordinates"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.io.bed6 import parse_bed6
    from minigen.core.fasta import generate_by_bed6
    fasta_records = parse_fasta(input_file)
    bed6_records = parse_bed6(bed6_file)
    extracted_records = generate_by_bed6(fasta_records, bed6_records)
    write_fasta(output_file, extracted_records)

@app.command("bed6-to-fasta-upstream")
def bed6_to_fasta_upstream(
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

@app.command("bed6-to-fasta-downstream")
def bed6_to_fasta_downstream(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file for downstream sequences"),
    bed6_file: str = typer.Argument(..., help="path to bed6 file with feature coordinates"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.io.bed6 import parse_bed6
    from minigen.core.fasta import generate_downstream
    fasta_records = parse_fasta(input_file)
    bed6_records = parse_bed6(bed6_file)
    downstream_records = generate_downstream(fasta_records, bed6_records)
    write_fasta(output_file, downstream_records)
