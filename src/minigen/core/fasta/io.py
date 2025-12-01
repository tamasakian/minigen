#!/usr/bin/env python3

from Bio import SeqIO

def parse_fasta(path: str) -> list:
    return list(SeqIO.parse(path, "fasta"))

def write_fasta(path: str, records: list) -> None:
    SeqIO.write(records, path, "fasta")