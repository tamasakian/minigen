#!/usr/bin/env python3

from Bio import SeqIO
from minigen.utils.homologs import pivot_wider

def parse_fasta(path: str) -> list:
    records = list(SeqIO.parse(path, "fasta"))
    return records

def write_fasta(path: str, records: list) -> None:
    SeqIO.write(records, path, "fasta")

def build_fasta_by_homologs(path_dir: str, records: list, homologs: list) -> None:
    group2members = pivot_wider(homologs)
    for group, members in group2members.items():
        path = f"{path_dir}/{group}.fasta"
        records = [r for r in records if r.id in members]
        SeqIO.write(records, path, "fasta")