#!/usr/bin/env python3

from ete4 import Tree

def parse_tree(path: str) -> Tree:
    return Tree(path, parser=0)