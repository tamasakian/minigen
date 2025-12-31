#!/usr/bin/env python3

from collections import defaultdict

def get_tag(seqid: str) -> str | None:
    if "|" not in seqid:
        return None
    return seqid.split("|")[-1]

def to_homologs(records: list[dict]) -> list[dict]:
    group_id = set()
    new_records = []
    for record in records:
        qseqid, rseqid = record["qseqid"], record["rseqid"]
        if qseqid not in group_id:
            new_records.append({"group_id": qseqid, "member_id": qseqid})
            group_id.add(qseqid)
        new_records.append({"group_id": qseqid, "member_id": rseqid})
    return new_records

def extract_blast_by_qseqid(records: list[dict], filters: list[str]) -> list[dict]:
    new_records = []
    for record in records:
        if record["qseqid"] not in filters:
            continue
        new_records.append(record)
    return new_records

def identify_qseqid_with_tag_only(records: list[dict], tag_list: list[str]) -> list[str]:
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

def identify_qseqid_with_tag_any(records: list[dict], tag_list: list[str]) -> list[str]:
    allowed = set(tag_list)
    qry2tags = defaultdict(list)
    for record in records:
        qseqid = record["qseqid"]
        rseqid = record["rseqid"]
        tag = get_tag(rseqid)
        qry2tags[qseqid].append(tag)
    matched = []
    for qseqid, tags in qry2tags.items():
        if not any(tag in allowed for tag in tags):
            continue
        matched.append(qseqid)
    return matched

def identify_qseqid_with_tag_none(records: list[dict], tag_list: list[str]) -> list[str]:
    allowed = set(tag_list)
    qry2tags = defaultdict(list)
    for record in records:
        qseqid = record["qseqid"]
        rseqid = record["rseqid"]
        tag = get_tag(rseqid)
        qry2tags[qseqid].append(tag)
    matched = []
    for qseqid, tags in qry2tags.items():
        if any(tag in allowed for tag in tags):
            continue
        matched.append(qseqid)
    return matched

def identify_qseqid_with_tag_all(records: list[dict], tag_list: list[str]) -> list[str]:
    required = set(tag_list)
    qry2tags = defaultdict(list)
    for record in records:
        qseqid = record["qseqid"]
        rseqid = record["rseqid"]
        tag = get_tag(rseqid)
        qry2tags[qseqid].append(tag)
    matched = []
    for qseqid, tags in qry2tags.items():
        if not all(tag in tags for tag in required):
            continue
        matched.append(qseqid)
    return matched

