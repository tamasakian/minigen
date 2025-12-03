#!/usr/bin/env python3

def parse_text(path: str) -> list[str]:
    records = []
    with open(path, "r") as handle:
        for line in handle:
            records.append(line.strip())
    return records

def write_text(path: str, records: list) -> None:
    with open(path, "w") as handle:
        for record in records:
            handle.write(f"{record}\n")