#!/usr/bin/env python3

def extract_bed4mcscanx_by_chrom(records: list, filters: set[str]) -> list:
    new_records = []
    for record in records:
        if record["chrom"] not in filters:
            continue
        new_records.append(record)
    return new_records

def extract_bed4mcscanx_by_name(records: list, filters: set[str]) -> list:
    new_records = []
    for record in records:
        if record["name"] not in filters:
            continue
        new_records.append(record)
    return new_records

def tag_bed4mcscanx_name(records: list, tag: str) -> list:
    new_records = []
    for record in records:
        new_name = f"{record["name"]}|{tag}"
        new_record = {
            "chrom": record["chrom"],
            "name": new_name,
            "start": record["start"],
            "end": record["end"]
        }
        new_records.append(new_record)
    return new_records