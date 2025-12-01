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

