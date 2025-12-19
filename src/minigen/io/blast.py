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

def write_blast(path: str, records: list[dict]) -> None:
    with open(path, mode="w") as handle:
        for record in records:
            qseqid = record["qseqid"]
            rseqid = record["rseqid"]
            pident = record["pident"]
            length = record["length"]
            mismatch = record["mismatch"]
            gapopen = record["gapopen"]
            qstart = record["qstart"]
            qend = record["qend"]
            rstart = record["rstart"]
            rend = record["rend"]
            evalue = record["evalue"]
            bitscore = record["bitscore"]
            line = "\t".join(map(str, [qseqid, rseqid, pident, length, mismatch, gapopen, qstart, qend, rstart, rend, evalue, bitscore]))
            handle.write(line + "\n")
