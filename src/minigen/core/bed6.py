#!/usr/bin/env python3

from collections import defaultdict
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

def generate_intron(records: list[dict[str, str]]) -> list[dict[str, str]]:
    cds_by_gene: dict[str, list[tuple[str, int, int, str]]] = defaultdict(list)
    for record in records:
        cds_by_gene[record["name"]].append((record["chrom"], record["start"], record["end"], record["strand"]))
    intron_records: list[dict] = []
    for name, cds_list in cds_by_gene.items():
        cds_list.sort(key=lambda x: x[1])
        chrom = cds_list[0][0]
        strand = cds_list[0][3]
        for i in range(len(cds_list)-1):
            intron_start = cds_list[i][2]
            intron_end = cds_list[i+1][1]
            if intron_end <= intron_start:
                continue
            intron_records.append({
                "chrom": chrom,
                "start": intron_start,
                "end": intron_end,
                "name": f"{name}_intron_{i+1}",
                "score": ".",
                "strand": strand,
            })
    return intron_records