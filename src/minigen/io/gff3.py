#!/usr/bin/env python3

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

def write_gff3(path: str, records: list) -> None:
    with open(path, "w") as handle:
        handle.write("##gff-version 3\n")
        for record in records:
            seqid = record["seqid"]
            source = record["source"]
            type_ = record["type"]
            start = record["start"]
            end = record["end"]
            score = record["score"]
            strand = record["strand"]
            phase = record["phase"]
            attributes = ";".join([f"{key}={value}" for key, value in record["attributes"].items()])
            line = "\t".join(map(str, [seqid, source, type_, start, end, score, strand, phase, attributes]))
            handle.write(line + "\n")