#!/usr/bin/env python3

from ete4 import Tree

def get_tag(leaf_name: str) -> str | None:
    if "|" not in leaf_name:
        return None
    return leaf_name.split("|")[-1]

def has_bipartite_tag_monophyly(tree: Tree, tag_list1: list[str], tag_list2: list[str]) -> bool:
    tag_set1 = set(tag_list1)
    tag_set2 = set(tag_list2)
    allowed = tag_set1 | tag_set2
    for node in tree.traverse("postorder"):
        names = list(node.leaf_names())
        if len(names) < 2:
            continue
        tags = []
        for name in names:
            tag = get_tag(name)
            if tag is None:
                break
            tags.append(tag)
        else:
            tagset = set(tags)
            if not tagset.issubset(allowed):
                continue
            if not (tagset & tag_set1 and tagset & tag_set2):
                continue
            return True
    return False
