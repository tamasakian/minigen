#!/usr/bin/env python3

def parse_blast(path: str) -> list[dict]:
    records = []
    with open(path, mode="r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 12:
                continue
            qseqid, rseqid, pident, length, mismatch, gapopen, qstart, qend, rstart, rend, evalue, bitscore = cols
            record = {
                "qseqid": qseqid,
                "rseqid":rseqid,
                "pident": pident,
                "length": length,
                "mismatch": mismatch,
                "gapopen": gapopen,
                "qstart": qstart,
                "qend": qend,
                "rstart": rstart,
                "rend": rend,
                "evalue": evalue,
                "bitscore": bitscore}
            records.append(record)
    return records