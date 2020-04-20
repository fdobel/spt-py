from typing import List

from spt.tree import NodeBuilder, _Node


def construction0(node_name: int):
    node = NodeBuilder().leaf(str(node_name))
    return node, [node]


def single_node_at(current_node, idx_path, depth, name):
    bld = NodeBuilder()
    if depth == 1:
        l = bld.leaf(name)
        if idx_path == 1:  # right node
            return bld.mid(current_node.left.child, l)
        else:
            return bld.only_left_child(l)

    if depth == 0:
        return bld.leaf(name)

    mask = 1 << (depth - 1)
    dir_right = idx_path & mask != 0
    if dir_right:
        return bld.mid(current_node.left.child, single_node_at(current_node.right.child, idx_path - mask, depth - 1, name))
    return bld.only_left_child(single_node_at(current_node.left.child, idx_path, depth - 1, name))


def construction1(root: _Node, source_nodes: List[int]):
    bld = NodeBuilder()

    av_nodes = len(root.leaf_nodes)
    if len(root.leaf_nodes) >= 2 ** root.depth:
        return bld.mid(root, bld.leaf(str(av_nodes))), source_nodes + [root]

    raise NotImplementedError


#def  construction2():
