#!/usr/bin/env python3

def query_bed(records: list, feat_type: str, attr_key: str) -> list:
    results = []
    for record in records:
        if record["type"] != feat_type:
            continue
        attrs = record["attributes"]
        if attr_key not in attrs:
            continue
        results.append((record["seqid"], attrs[attr_key], record["start"], record["end"]))
    return results

def filter_records(records: list, filter_file: str) -> list:
    new_records = []
    with open(filter_file, "r") as filter_handle:
        filters = set(line.strip() for line in filter_handle)
    for record in records:
        seqid, gene_id, start, end = record
        if gene_id not in filters:
            continue
        new_records.append(record)
    return new_records