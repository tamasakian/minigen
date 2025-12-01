#!/usr/bin/env python3

import typer
from minigen.core.fasta.io import parse_fasta, write_fasta
from minigen.core.fasta.utils import suffix_headers, filter_records

app = typer.Typer()

@app.command("add-tag")
def add_tag(input_file: str, output_file: str, tag: str) -> None:
    records = parse_fasta(input_file)
    new_records = suffix_headers(records, tag)
    write_fasta(output_file, new_records)

@app.command("filter")
def filter_fasta(input_file: str, output_file: str, filter_file: str) -> None:
    records = parse_fasta(input_file)
    new_records = filter_records(records, filter_file)
    write_fasta(output_file, new_records)