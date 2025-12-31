#!/usr/bin/env python3

def write_homology_table(path: str, records: list[dict]) -> None:
    with open(path, "w") as handle:
        for record in records:
            qseqid = record["qseqid"]
            rseqid = record["rseqid"]
            line = "\t".join([qseqid, rseqid])
            handle.write(line + "\n")