#!/usr/bin/env python3

from Bio.SeqRecord import SeqRecord

def suffix_headers(records: list[SeqRecord], suffix: str) -> list[SeqRecord]:
    new_records = []
    for record in records:
        new_id = f"{record.id}|{suffix}"
        new_record = SeqRecord(
            seq=record.seq,
            id=new_id,
            description=""
        )
        new_records.append(new_record)
    return new_records

def filter_records(records: list[SeqRecord], filter_file: str) -> list[SeqRecord]:
    new_records = []
    with open(filter_file, "r") as filter_handle:
        filters = set(line.strip() for line in filter_handle)
    for record in records:
        if record.id not in filters:
            continue
        new_records.append(record)
    return new_records

