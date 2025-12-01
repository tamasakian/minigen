#!/usr/bin/env python3

def query_canonical(records: list) -> list:
    canonical_list = []
    for record in records:
        if record["type"] != "mRNA":
            continue
        attrs = record["attributes"]
        if attrs.get("tag") != "Ensembl_canonical":
            continue
        canonical_list.append(attrs.get("transcript_id"))
    return canonical_list