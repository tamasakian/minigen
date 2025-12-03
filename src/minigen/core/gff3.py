#!/usr/bin/env python3

def extract_gff3_by_seqid(records: list, filters: list[str]) -> list:
    new_records = []
    for record in records:
        if record["seqid"] not in filters:
            continue
        new_records.append(record)
    return new_records

def extract_gff3_by_type(records: list, filters: list[str]) -> list:
    new_records = []
    for record in records:
        if record["type"] not in filters:
            continue
        new_records.append(record)
    return new_records

def extract_gff3_by_attributes(records: list, filters: list[str], key: str) -> list:
    new_records = []
    for record in records:
        attrs = record["attributes"]
        if key not in attrs:
            continue
        if attrs[key] not in filters:
            continue
        new_records.append(record)
    return new_records

def to_bed6(records: list, key: str) -> list:
    bed6_records = []
    for record in records:
        attrs = record["attributes"]
        if key not in attrs:
            continue
        chrom = record["seqid"]
        start = int(record["start"]) - 1
        end = int(record["end"])
        name = attrs[key]
        score = record["score"]
        strand = record["strand"]
        bed6_record = {"chrom": chrom, "start": start, "end": end, "name": name, "score": score, "strand": strand}
        bed6_records.append(bed6_record)
    return bed6_records

def to_mcscanx_bed4(records: list, key: str) -> list:
    bed4_records = []
    for record in records:
        attrs = record["attributes"]
        if key not in attrs:
            continue
        chrom = record["seqid"]
        name = attrs[key]
        start = int(record["start"]) - 1
        end = int(record["end"])
        bed4_record = {"chrom": chrom, "name": name, "start": start, "end": end}
        bed4_records.append(bed4_record)
    return bed4_records

def identify_canonical(records: list) -> list[str]:
    canonical_ids = []
    for record in records:
        if record["type"] != "mRNA":
            continue
        attrs = record["attributes"]
        if not "tag" in attrs:
            continue
        if attrs["tag"] != "Ensembl_canonical":
            continue
        if not "transcript_id" in attrs:
            continue
        canonical_ids.append(attrs["transcript_id"])
    return canonical_ids