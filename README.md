# minigen

`minigen` is a minimal command-line toolkit for small genome annotation,
sequence, BLAST, homolog-group, and tree-processing tasks.

## Installation

Install the package in an environment with Python 3.9 or newer:

```bash
pip install git+https://github.com/tamasakian/rbhmap.git
```

The package provides the `minigen` command.

## Command Overview

Most commands follow this pattern:

```bash
minigen <command-group> <command> <input-file> <output-file> [extra-arguments]
```

Text-list inputs are plain text files with one identifier or tag per line.
FASTA inputs and outputs use standard FASTA format. BLAST inputs and outputs
use tabular BLAST outfmt 6 with 12 columns.

## `build`

Commands that build multiple output files from a larger input collection.

### `build fasta-homologs`

```bash
minigen build fasta-homologs <input-fasta> <output-dir> <homologs-file>
```

Reads a FASTA file and a two-column homologs file containing `group_id` and
`member_id`. It writes one FASTA file per homolog group into the output
directory, containing the sequences whose FASTA identifiers match the group
members.

## `collect`

Commands that collect records from another format into a compact summary.

### `collect blast-to-homologs`

```bash
minigen collect blast-to-homologs <input-blast> <output-homologs>
```

Reads tabular BLAST outfmt 6. For each query sequence, it creates homolog-group
records where the query ID is the `group_id` and both the query and matching
reference IDs are emitted as `member_id` values. The output is a two-column
tab-separated homologs file.

## `detect`

Commands that detect whether an input satisfies a condition.

### `detect tree-bipartite-monophyly`

```bash
minigen detect tree-bipartite-monophyly <input-newick> <group1-tags.txt> <group2-tags.txt>
```

Reads a Newick tree and two text files of leaf-name tags. Leaf tags are taken
from the final `|`-delimited field of each leaf name. If the tree contains a
node whose descendant leaves include tags from both groups and only tags from
the two supplied groups, the command prints the input tree filename to stdout.
If no such node is found, it prints nothing.

## `extract`

Commands that filter records by identifiers, feature fields, attributes, or
minimum group size.

### `extract fasta`

```bash
minigen extract fasta <input-fasta> <output-fasta> <ids.txt>
```

Reads a FASTA file and a text file of sequence IDs. It writes a FASTA file
containing only records whose FASTA ID is listed in the text file.

### `extract gff3-seqid`

```bash
minigen extract gff3-seqid <input-gff3> <output-gff3> <seqids.txt>
```

Reads a GFF3 file and a text file of sequence IDs. It writes a GFF3 file
containing only records whose `seqid` column matches the supplied list.

### `extract gff3-type`

```bash
minigen extract gff3-type <input-gff3> <output-gff3> <types.txt>
```

Reads a GFF3 file and a text file of feature types, such as `gene`, `mRNA`, or
`CDS`. It writes a GFF3 file containing only records whose type column matches
the supplied list.

### `extract gff3-attributes`

```bash
minigen extract gff3-attributes <input-gff3> <output-gff3> <ids.txt> <attribute-key>
```

Reads a GFF3 file, a text file of accepted attribute values, and an attribute
key such as `ID`, `transcript_id`, or `protein_id`. It writes a GFF3 file
containing only records whose selected attribute exists and has a value listed
in the text file.

### `extract bed4mcscanx-chrom`

```bash
minigen extract bed4mcscanx-chrom <input-bed4> <output-bed4> <chroms.txt>
```

Reads an MCScanX-style BED4 file and a text file of chromosome names. It writes
a BED4 file containing only records whose chromosome field is listed.

### `extract bed4mcscanx-name`

```bash
minigen extract bed4mcscanx-name <input-bed4> <output-bed4> <names.txt>
```

Reads an MCScanX-style BED4 file and a text file of feature names. It writes a
BED4 file containing only records whose name field is listed.

### `extract blast-qseqid`

```bash
minigen extract blast-qseqid <input-blast> <output-blast> <query-ids.txt>
```

Reads tabular BLAST outfmt 6 and a text file of query IDs. It writes a BLAST
outfmt 6 file containing only alignments whose `qseqid` is listed.

### `extract homologs-min-size`

```bash
minigen extract homologs-min-size <input-homologs> <output-homologs> <min-size>
```

Reads a two-column homologs file with `group_id` and `member_id`. It writes a
homologs file containing only groups with at least `min-size` member records.

## `generate`

Commands that generate derived coordinates or sequences.

### `generate bed6-upstream`

```bash
minigen generate bed6-upstream <input-bed6> <output-bed6> <bp>
```

Reads BED6 feature coordinates and writes BED6 intervals immediately upstream
of each feature. For `+` strand features, upstream means `start - bp` to
`start`; for `-` strand features, upstream means `end` to `end + bp`. Output
names are suffixed with `|upstream|<bp>`.

### `generate bed6-downstream`

```bash
minigen generate bed6-downstream <input-bed6> <output-bed6> <bp>
```

Reads BED6 feature coordinates and writes BED6 intervals immediately downstream
of each feature. For `+` strand features, downstream means `end` to `end + bp`;
for `-` strand features, downstream means `start - bp` to `start`. Output names
are suffixed with `|downstream|<bp>`.

### `generate bed6-intron`

```bash
minigen generate bed6-intron <input-bed6> <output-bed6>
```

Reads BED6 CDS coordinates grouped by the BED name field. It writes BED6 intron
intervals between adjacent CDS intervals for each name. Output names use the
form `<name>_intron_<number>`.

### `generate fasta-reverse-complement`

```bash
minigen generate fasta-reverse-complement <input-fasta> <output-fasta>
```

Reads FASTA sequences and writes their reverse complements. Output FASTA IDs are
suffixed with `|reverse_complement`.

### `generate fasta-cds-to-protein`

```bash
minigen generate fasta-cds-to-protein <input-fasta> <output-fasta>
```

Reads FASTA CDS nucleotide sequences and writes translated protein sequences.
Translation stops at the first stop codon. Output FASTA IDs are suffixed with
`|protein`.

## `identify`

Commands that identify IDs matching annotation or BLAST-tag criteria and write
plain text ID lists.

### `identify ensembl-canonical`

```bash
minigen identify ensembl-canonical <input-gff3> <output.txt>
```

Reads a GFF3 file and writes transcript IDs for `mRNA` records whose `tag`
attribute is `Ensembl_canonical` and whose `transcript_id` attribute is present.

### `identify augustus-longest`

```bash
minigen identify augustus-longest <input-gff3> <output.txt> <attribute-key>
```

Reads a GFF3 file and identifies the longest CDS-supported transcript per gene.
CDS lengths are summed by the selected attribute key, and transcript IDs are
grouped by the prefix before `.t`. The output is a text file of the longest
transcript IDs.

### `identify blast-tag-only`

```bash
minigen identify blast-tag-only <input-blast> <output.txt> <tags.txt>
```

Reads tabular BLAST outfmt 6 and a text file of accepted tags. Tags are taken
from the final `|`-delimited field of each reference sequence ID. It writes
query IDs for which every BLAST hit has one of the accepted tags.

### `identify blast-tag-any`

```bash
minigen identify blast-tag-any <input-blast> <output.txt> <tags.txt>
```

Reads tabular BLAST outfmt 6 and writes query IDs that have at least one hit
whose reference sequence tag is listed in the tag file.

### `identify blast-tag-none`

```bash
minigen identify blast-tag-none <input-blast> <output.txt> <tags.txt>
```

Reads tabular BLAST outfmt 6 and writes query IDs that have no hits whose
reference sequence tag is listed in the tag file.

### `identify blast-tag-all`

```bash
minigen identify blast-tag-all <input-blast> <output.txt> <tags.txt>
```

Reads tabular BLAST outfmt 6 and writes query IDs whose set of hit tags contains
all tags listed in the tag file.

## `tag`

Commands that append a tag to sequence or feature names.

### `tag fasta`

```bash
minigen tag fasta <input-fasta> <output-fasta> <tag>
```

Reads FASTA records and writes a FASTA file whose sequence IDs are suffixed with
`|<tag>`. Sequence content is unchanged.

### `tag bed4mcscanx-name`

```bash
minigen tag bed4mcscanx-name <input-bed4> <output-bed4> <tag>
```

Reads an MCScanX-style BED4 file and writes a BED4 file whose name field is
suffixed with `|<tag>`. Coordinates are unchanged.

## `transform`

Commands that convert between supported genome-analysis formats.

### `transform gff3-to-text`

```bash
minigen transform gff3-to-text <input-gff3> <output.txt> <attribute-key>
```

Reads a GFF3 file and writes a plain text list of values from the selected
attribute key, such as `ID`, `transcript_id`, or `protein_id`. Records that do
not contain the attribute key are skipped.

### `transform gff3-to-bed6`

```bash
minigen transform gff3-to-bed6 <input-gff3> <output-bed6> <attribute-key>
```

Reads a GFF3 file and writes BED6 records. The GFF3 `seqid`, `start`, `end`,
`score`, and `strand` fields become the corresponding BED fields, GFF3 starts
are converted from 1-based to 0-based coordinates, and the selected attribute
value becomes the BED name.

### `transform gff3-to-bed4mcscanx`

```bash
minigen transform gff3-to-bed4mcscanx <input-gff3> <output-bed4> <attribute-key>
```

Reads a GFF3 file and writes MCScanX-style BED4 records containing chromosome,
name, start, and end fields. The selected GFF3 attribute value becomes the BED4
name, and GFF3 starts are converted from 1-based to 0-based coordinates.

### `transform blast-to-bed6`

```bash
minigen transform blast-to-bed6 <input-blast> <output-bed6>
```

Reads tabular BLAST outfmt 6 and writes BED6 intervals on the reference
sequence. The BED name combines reference ID, query ID, and query coordinates;
the BED score is the BLAST bitscore; and the strand is inferred from query and
reference coordinate direction.

### `transform bed6-to-fasta`

```bash
minigen transform bed6-to-fasta <input-fasta> <output-fasta> <input-bed6>
```

Reads genome FASTA sequences and BED6 intervals. It writes a FASTA file
containing the sequence for each interval, using the BED name as the FASTA ID.
Intervals on the `-` strand are reverse-complemented.

### `transform bed6-to-fasta-upstream`

```bash
minigen transform bed6-to-fasta-upstream <input-fasta> <output-fasta> <input-bed6>
```

Reads genome FASTA sequences and BED6 upstream intervals, then writes the
corresponding FASTA sequences. Regions outside chromosome bounds are padded with
`N`, and `-` strand intervals are reverse-complemented.

### `transform bed6-to-fasta-downstream`

```bash
minigen transform bed6-to-fasta-downstream <input-fasta> <output-fasta> <input-bed6>
```

Reads genome FASTA sequences and BED6 downstream intervals, then writes the
corresponding FASTA sequences. Regions outside chromosome bounds are padded with
`N`, and `-` strand intervals are reverse-complemented.
