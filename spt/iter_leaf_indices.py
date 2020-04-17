from spt.tree import NodeBuilder


def find_leaf(node, leaf_idx):

    if node.depth is None:
        raise RuntimeError("depth is not set")
    mask = 1 << (node.depth - 1)
    while mask > 0:
        if mask & leaf_idx == 0:
            yield "left"
        else:
            yield "right"
        mask = mask >> 1


def distance_common_ancestor(tree_depth, idx1, idx2):
    mask = 1 << tree_depth - 1
    c = idx1 ^ idx2
    count = 0
    while mask & c == 0:
        count += 1
        mask = mask >> 1
    distance_to_common_ancestor = tree_depth - count
    return distance_to_common_ancestor


def tree_node_to_node(node, node_path, leaf_indices):

    next_idx = leaf_indices[0]

    if len(leaf_indices) > 1:
        look_forward = leaf_indices[1]
    else:
        look_forward = None

    lu = node_path[len(node_path) - 1]

    if next_idx >= 1 << node.depth:
        raise RuntimeError("leaf (%i) does not exist (depth %i)" % (next_idx, node.depth))

    for direction in find_leaf(lu, next_idx):
        yield direction
        if direction == 'left':
            lu = lu.left.child
            node_path.append(lu)

        if direction == 'right':
            lu = lu.right.child
            node_path.append(lu)

    if look_forward is not None:
        dca = distance_common_ancestor(node.depth, next_idx, look_forward)
        for _ in range(dca):
            yield "up"

        for t in tree_node_to_node(node, node_path[:-dca], leaf_indices[1:]):
            yield t
