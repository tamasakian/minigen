#!/usr/bin/env python3

from copy import copy

def generate_upstream(records: list[dict[str, str]], bp: int) -> list[dict[str, str]]:
    upstream_records = []
    for record in records:
        start = int(record["start"])
        end = int(record["end"])
        name = record["name"]
        strand = record["strand"]
        if strand == "+":
            upstream_start = start - bp
            upstream_end = start
        elif strand == "-":
            upstream_start = end
            upstream_end = end + bp
        else:
            continue
        upstream_record = copy(record)
        upstream_record["start"] = upstream_start
        upstream_record["end"] = upstream_end
        upstream_record["name"] = f"{name}|upstream|{bp}"
        upstream_records.append(upstream_record)
    return upstream_records

