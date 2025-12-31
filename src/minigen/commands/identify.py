#!/usr/bin/env python3

import typer
from minigen.io.text import write_text

app = typer.Typer(help="identify tools")

@app.command("ensembl-canonical")
def ensembl_canonical(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import identify_canonical
    records = parse_gff3(input_file)
    canonical_ids = identify_canonical(records)
    write_text(output_file, canonical_ids)

@app.command("augustus-longest")
def augustus_longest(
    input_file: str = typer.Argument(..., help="path to input gff3 file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
    attr_key: str = typer.Argument(..., help="attribute key"),
):
    from minigen.io.gff3 import parse_gff3
    from minigen.core.gff3 import identify_longest
    records = parse_gff3(input_file)
    longest_ids = identify_longest(records, attr_key)
    write_text(output_file, longest_ids)

@app.command("blast-tag-only")
def blast_tag_only(
    input_file: str = typer.Argument(..., help="path to input blast file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
    text_file: str = typer.Argument(..., help="path to text file with tags to identify"),
):
    from minigen.io.blast import parse_blast
    from minigen.io.text import parse_text
    from minigen.core.blast import identify_qseqid_with_tag_only
    records = parse_blast(input_file)
    tag_list = parse_text(text_file)
    qry_list = identify_qseqid_with_tag_only(records, tag_list)
    write_text(output_file, qry_list)

@app.command("blast-tag-any")
def blast_tag_any(
    input_file: str = typer.Argument(..., help="path to input blast file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
    text_file: str = typer.Argument(..., help="path to text file with tags to identify"),
):
    from minigen.io.blast import parse_blast
    from minigen.io.text import parse_text
    from minigen.core.blast import identify_qseqid_with_tag_any
    records = parse_blast(input_file)
    tag_list = parse_text(text_file)
    qry_list = identify_qseqid_with_tag_any(records, tag_list)
    write_text(output_file, qry_list)

@app.command("blast-tag-none")
def blast_tag_none(
    input_file: str = typer.Argument(..., help="path to input blast file"),
    output_file: str = typer.Argument(..., help="path to output text file"),
    text_file: str = typer.Argument(..., help="path to text file with tags to identify"),
):
    from minigen.io.blast import parse_blast
    from minigen.io.text import parse_text
    from minigen.core.blast import identify_qseqid_with_tag_none
    records = parse_blast(input_file)
    tag_list = parse_text(text_file)
    qry_list = identify_qseqid_with_tag_none(records, tag_list)
    write_text(output_file, qry_list)