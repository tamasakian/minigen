#!/usr/bin/env python3

from Bio import SeqIO

def parse_fasta(path: str) -> list:
    records = list(SeqIO.parse(path, "fasta"))
    return records

def write_fasta(path: str, records: list) -> None:
    SeqIO.write(records, path, "fasta")