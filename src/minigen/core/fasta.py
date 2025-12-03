#!/usr/bin/env python3

from Bio.SeqRecord import SeqRecord

def extract_fasta(records: list[SeqRecord], filters: list[str]) -> list[SeqRecord]:
    new_records = []
    for record in records:
        if record.id not in filters:
            continue
        new_records.append(record)
    return new_records

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