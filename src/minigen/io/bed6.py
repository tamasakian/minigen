#!/usr/bin/env python3

def write_bed6(path: str, records: list) -> None:
    with open(path, "w") as handle:
        for record in records:
            chrom = record["chrom"]
            start = record["start"]
            end = record["end"]
            name = record["name"]
            score = record["score"]
            strand = record["strand"]
            line = "\t".join(map(str, [chrom, start, end, name, score, strand]))
            handle.write(line + "\n")
