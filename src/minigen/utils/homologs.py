#!/usr/bin/env python3

from collections import defaultdict

def pivot_wider(records: list[dict]) -> dict[str, set[str]]:
    group2members: dict[str, set[str]] = defaultdict(set)
    for record in records:
        group2members[record["group_id"]].add(record["member_id"])
    return group2members