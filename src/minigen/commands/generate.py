#!/usr/bin/env python3

import typer

app = typer.Typer(help="generate tools")

@app.command("bed6-upstream")
def bed6_upstream(
    input_file: str = typer.Argument(..., help="path to input bed6 file (gene coordinates)"),
    output_file: str = typer.Argument(..., help="path to output bed6 file for upstream"),
    bp: str = typer.Argument(..., help="number of base pairs upstream to extract"),
):
    from minigen.io.bed6 import parse_bed6, write_bed6
    from minigen.core.bed6 import generate_upstream
    records = parse_bed6(input_file)
    upstream_records = generate_upstream(records, int(bp))
    write_bed6(output_file, upstream_records)

@app.command("bed6-downstream")
def bed6_downstream(
    input_file: str = typer.Argument(..., help="path to input bed6 file (gene coordinates)"),
    output_file: str = typer.Argument(..., help="path to output bed6 file for downstream"),
    bp: str = typer.Argument(..., help="number of base pairs downstream to extract"),
):
    from minigen.io.bed6 import parse_bed6, write_bed6
    from minigen.core.bed6 import generate_downstream
    records = parse_bed6(input_file)
    downstream_records = generate_downstream(records, int(bp))
    write_bed6(output_file, downstream_records)

@app.command("bed6-intron")
def bed6_intron(
    input_file: str = typer.Argument(..., help="path to input bed6 file (cds coordinates)"),
    output_file: str = typer.Argument(..., help="path to output bed6 file for intron"),
):
    from minigen.io.bed6 import parse_bed6, write_bed6
    from minigen.core.bed6 import generate_intron
    records = parse_bed6(input_file)
    intron_records = generate_intron(records)
    write_bed6(output_file, intron_records)

@app.command("fasta-reverse-complement")
def fasta_reverse_complement(
    input_file: str = typer.Argument(..., help="path to input fasta file"),
    output_file: str = typer.Argument(..., help="path to output fasta file for reverse complement sequences"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.core.fasta import generate_reverse_complement
    records = parse_fasta(input_file)
    rc_records = generate_reverse_complement(records)
    write_fasta(output_file, rc_records)

@app.command("fasta-cds-to-protein")
def fasta_cds_to_protein(
    input_file: str = typer.Argument(..., help="path to input fasta file with CDS sequences"),
    output_file: str = typer.Argument(..., help="path to output fasta file for protein sequences"),
):
    from minigen.io.fasta import parse_fasta, write_fasta
    from minigen.core.fasta import generate_cds_to_protein
    records = parse_fasta(input_file)
    protein_records = generate_cds_to_protein(records)
    write_fasta(output_file, protein_records)