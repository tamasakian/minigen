#!/usr/bin/env python3

import typer
from minigen.core.mcscanx.io import parse_gff3, write_bed
from minigen.core.mcscanx.utils import query_bed

app = typer.Typer()

@app.command("convert")
def gff3_to_bed(
    input_file: str = typer.Argument(..., help="path to input gff3"),
    output_file: str = typer.Argument(..., help="path to output bed"),
    feat_type: str = typer.Argument(..., help="feature type to extract (e.g., mRNA, gene)"),
    attr_key: str = typer.Argument(..., help="attribute key for gene ID (e.g., transcript_id, ID)"),
):
    records = parse_gff3(input_file)
    bed_list = query_bed(records, feat_type, attr_key)
    write_bed(output_file, bed_list)