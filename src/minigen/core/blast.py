#!/usr/bin/env python3

from collections import defaultdict

def get_tag(seqid: str) -> str | None:
    if "|" not in seqid:
        return None
    return seqid.split("|")[-1]

def extract_blast_by_qseqid(records: list, filters: list[str]) -> list:
    new_records = []
    for record in records:
        if record["qseqid"] not in filters:
            continue
        new_records.append(record)
    return new_records

def identify_qry_with_tagonly(records: list[dict], tag_list: list[str]) -> list[str]:
    allowed = set(tag_list)
    qry2tags = defaultdict(list)
    for record in records:
        qseqid = record["qseqid"]
        rseqid = record["rseqid"]
        tag = get_tag(rseqid)
        qry2tags[qseqid].append(tag)
    matched = []
    for qseqid, tags in qry2tags.items():
        if not all(tag in allowed for tag in tags):
            continue
        matched.append(qseqid)
    return matched