#!/usr/bin/env python3

def parse_bed4mcscanx(path: str) -> list[list[str]]:
    records = []
    with open(path, "r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 4:
                continue
            chrom, name, start, end = cols
            record = {"chrom": chrom, "name": name, "start": start, "end": end}
            records.append(record)
    return records

def write_bed4mcscanx(path: str, records: list[dict]) -> None:
    with open(path, "w") as handle:
        for record in records:
            chrom = record["chrom"]
            name = record["name"]
            start = record["start"]
            end = record["end"]
            line = "\t".join(map(str, [chrom, name, start, end]))
            handle.write(line + "\n")