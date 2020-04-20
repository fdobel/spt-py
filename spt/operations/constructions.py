from typing import List

from spt.tree import NodeBuilder, _Node


def construction0(node_name: int):
    node = NodeBuilder().leaf(str(node_name))
    return node, [node]


def construction1(root: _Node, source_nodes: List[int]):

    return 0, source_nodes + [root]
    # todo
