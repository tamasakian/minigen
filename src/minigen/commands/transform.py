#!/usr/bin/env python3

import typer

app = typer.Typer(help="transform tools")

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

@app.command("gff3-to-mcscanx-bed4")
def gff3_to_mcscanx_bed4(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output mcscanx bed4 file"),
    attr_key: str = typer.Argument(..., help="attribute key for bed4 names (e.g., ID, transcript_id, protein_id)"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import to_mcscanx_bed4
    from minigen.io.mcscanx_bed4 import write_mcscanx_bed4
    records = parse_gff3(input_file)
    bed4_records = to_mcscanx_bed4(records, attr_key)
    write_mcscanx_bed4(output_file, bed4_records)

