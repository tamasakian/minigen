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
