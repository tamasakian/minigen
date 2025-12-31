#!/usr/bin/env python3

from collections import Counter

def extract_homologs_by_min_size(records: list[dict], min_size: int) -> list[dict]:
    group_list = [record["group_id"] for record in records]
    group2count = Counter(group_list)
    new_records = []
    for record in records:
        if group2count[record["group_id"]] < int(min_size):
            continue
        new_records.append(record)
    return new_records
