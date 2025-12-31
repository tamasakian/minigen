#!/usr/bin/env python3

def parse_homologs(path: str) -> list[dict]:
    records = []
    with open(path, "r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 2:
                continue
            group_id, member_id = cols
            record = {"group_id": group_id, "member_id": member_id}
            records.append(record)
    return records

def write_homologs(path: str, records: list[dict]) -> None:
    with open(path, "w") as handle:
        for record in records:
            group_id = record["group_id"]
            member_id = record["member_id"]
            line = "\t".join([group_id, member_id])
            handle.write(line + "\n")