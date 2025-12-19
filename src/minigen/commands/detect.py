#!/usr/bin/env python3

import typer

app = typer.Typer(help="detect tools")

@app.command("tree-bipartite-monophyly")
def tree_bipartite_monophyly(
    input_file: str = typer.Argument(..., help="path to input newick file"),
    text_file1: str = typer.Argument(..., help="path to text file with tags to detect (group 1)"),
    text_file2: str = typer.Argument(..., help="path to text file with tags to detect (group 2)"),
):
    from minigen.io.tree import parse_tree
    from minigen.io.text import parse_text
    from minigen.core.tree import has_bipartite_tag_monophyly
    from minigen.io.stdout import print_filename
    tree = parse_tree(input_file)
    tag_list1 = parse_text(text_file1)
    tag_list2 = parse_text(text_file2)
    if has_bipartite_tag_monophyly(tree, tag_list1, tag_list2):
        print_filename(input_file)
