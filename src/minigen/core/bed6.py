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

def generate_downstream(records: list[dict[str, str]], bp: int) -> list[dict[str, str]]:
    downstream_records = []
    for record in records:
        start = int(record["start"])
        end = int(record["end"])
        name = record["name"]
        strand = record["strand"]
        if strand == "+":
            downstream_start = end
            downstream_end = end + bp
        elif strand == "-":
            downstream_start = start - bp
            downstream_end = start
        else:
            continue
        downstream_record = copy(record)
        downstream_record["start"] = downstream_start
        downstream_record["end"] = downstream_end
        downstream_record["name"] = f"{name}|downstream|{bp}"
        downstream_records.append(downstream_record)
    return downstream_records
