#!/usr/bin/env python3

# core/io.py

def parse_gff3(path: str) -> list:
    records = []
    with open(path, "r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 9:
                continue
            seqid, source, type_, start, end, score, strand, phase, attributes = cols
            attr_cols = {}
            for attr in attributes.split(";"):
                if not attr:
                    continue
                if "=" not in attr:
                    continue
                key, value = attr.split("=", 1)
                attr_cols[key] = value
            record = {"seqid": seqid, "source": source, "type": type_, "start": start, "end": end, "score": score, "strand": strand, "phase": phase, "attributes": attr_cols}
            records.append(record)
    return records

def parse_bed(path: str) -> list:
    bed_list = []
    with open(path, "r") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            cols = line.strip().split("\t")
            if len(cols) != 4:
                continue
            seqid, gene_id, start, end = cols
            bed_list.append((seqid, gene_id, start, end))
    return bed_list

def write_bed(path: str, bed_list: list) -> None:
    with open(path, "w") as out:
        for seqid, gene_id, start, end in bed_list:
            out.write(f"{seqid}\t{gene_id}\t{start}\t{end}\n")
