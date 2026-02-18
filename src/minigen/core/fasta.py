#!/usr/bin/env python3

from copy import copy

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def extract_fasta(records: list[SeqRecord], filters: list[str]) -> list[SeqRecord]:
    new_records = []
    for record in records:
        if record.id not in filters:
            continue
        new_records.append(record)
    return new_records

def generate_by_bed6(fasta_records: list[SeqRecord], bed6_records: list[dict[str, str]]) -> list[SeqRecord]:
    fasta_dict = {record.id: record for record in fasta_records}
    new_records = []
    for bed in bed6_records:
        chrom = bed["chrom"]
        start = int(bed["start"])
        end = int(bed["end"])
        name = bed["name"]
        strand = bed["strand"]
        if chrom not in fasta_dict:
            continue
        chrom_record = fasta_dict[chrom]
        seq = chrom_record.seq
        lo = min(start, end)
        hi = max(start, end)
        extracted = str(seq[lo:hi])
        if strand == "-":
            extracted = str(Seq(extracted).reverse_complement())
        new_record = copy(chrom_record)
        new_record.id = name
        new_record.description = ""
        new_record.seq = Seq(extracted)
        new_records.append(new_record)
    return new_records

def generate_upstream(fasta_records: list[SeqRecord], bed6_records: list[dict[str, str]]) -> list[SeqRecord]:
    fasta_dict = {record.id: record for record in fasta_records}
    upstream_records = []
    for bed in bed6_records:
        chrom = bed["chrom"]
        start = int(bed["start"])
        end = int(bed["end"])
        name = bed["name"]
        strand = bed["strand"]
        if chrom not in fasta_dict:
            continue
        chrom_record = fasta_dict[chrom]
        seq = chrom_record.seq
        chrom_size = len(seq)
        upstream_start = max(0, start)
        upstream_end = min(chrom_size, end)
        extracted = ""
        if upstream_start > upstream_end:
            continue
        extracted = str(seq[upstream_start:upstream_end])
        start_pad = max(0, 0 - start)
        end_pad = max(0, end - chrom_size)
        padded_seq = Seq("N" * start_pad + extracted + "N" * end_pad)
        if strand == "-":
            padded_seq = padded_seq.reverse_complement()
        upstream_record = copy(chrom_record)
        upstream_record.id = name
        upstream_record.description = ""
        upstream_record.seq = padded_seq
        upstream_records.append(upstream_record)
    return upstream_records

def generate_downstream(fasta_records: list[SeqRecord], bed6_records: list[dict[str, str]]) -> list[SeqRecord]:
    fasta_dict = {record.id: record for record in fasta_records}
    downstream_records = []
    for bed in bed6_records:
        chrom = bed["chrom"]
        start = int(bed["start"])
        end = int(bed["end"])
        name = bed["name"]
        strand = bed["strand"]
        if chrom not in fasta_dict:
            continue
        chrom_record = fasta_dict[chrom]
        seq = chrom_record.seq
        chrom_size = len(seq)
        downstream_start = max(0, start)
        downstream_end = min(chrom_size, end)
        extracted = ""
        if downstream_start > downstream_end:
            continue
        extracted = str(seq[downstream_start:downstream_end])
        start_pad = max(0, 0 - start)
        end_pad = max(0, end - chrom_size)
        padded_seq = Seq("N" * start_pad + extracted + "N" * end_pad)
        if strand == "-":
            padded_seq = padded_seq.reverse_complement()
        downstream_record = copy(chrom_record)
        downstream_record.id = name
        downstream_record.description = ""
        downstream_record.seq = padded_seq
        downstream_records.append(downstream_record)
    return downstream_records

def tag_fasta(records: list[SeqRecord], tag: str) -> list[SeqRecord]:
    new_records = []
    for record in records:
        new_id = f"{record.id}|{tag}"
        new_record = SeqRecord(
            seq=record.seq,
            id=new_id,
            description=""
        )
        new_records.append(new_record)
    return new_records