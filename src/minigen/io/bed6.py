#!/usr/bin/env python3

def parse_bed6(path: str) -> list[dict[str, str]]:
    records = []
    with open(path, "r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 6:
                continue
            chrom, start, end, name, score, strand = cols
            record = {"chrom": chrom, "start": start, "end": end, "name": name, "score": score, "strand": strand}
            records.append(record)
    return records

def write_bed6(path: str, records: list) -> None:
    with open(path, "w") as handle:
        for record in records:
            chrom = record["chrom"]
            start = record["start"]
            end = record["end"]
            name = record["name"]
            score = record["score"]
            strand = record["strand"]
            fields = (chrom, start, end, name, score, strand)
            line = "\t".join(map(str, fields))
            handle.write(line + "\n")
