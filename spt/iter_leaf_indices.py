

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


def walk_tree(node, leaf_indices):
    """

    :param node: Root node
    :param leaf_indices: indices to navigate to.
    :return:
    """
    return nav_tree_node_to_node(node, [(node, 'root')], leaf_indices)


def nav_tree_node_to_node(node, node_path, leaf_indices):
    """

    :param node:
    :param node_path:
    :param leaf_indices:
    :return: generator of tuples (direction, weight).
    """
    next_idx = leaf_indices[0]

    if len(leaf_indices) > 1:
        look_forward = leaf_indices[1]
    else:
        look_forward = None

    lu = node_path[len(node_path) - 1][0]

    if next_idx >= 1 << node.depth:
        raise RuntimeError("leaf (%i) does not exist (depth %i)" % (next_idx, node.depth))

    for direction in find_leaf(lu, next_idx):

        if direction == 'left':
            yield direction, lu.left.weight
            lu = lu.left.child

        if direction == 'right':
            yield direction, lu.right.weight
            lu = lu.right.child
        node_path.append((lu, direction))

    if look_forward is not None:
        dca = distance_common_ancestor(node.depth, next_idx, look_forward)

        for pointer_last_directions in range(dca):

            # print(node_path)
            last_nodes_pointer = node_path[-1]
            up_node = node_path[-2][0]
            # print(last_nodes_pointer)

            if last_nodes_pointer[1] == 'left':
                weight = up_node.left.weight
            else:  # right
                weight = up_node.right.weight
            yield "up", weight
            node_path = node_path[:-1]
            # node_path.append((last_nodes_pointer[0], 'up'))

        for a in nav_tree_node_to_node(node, node_path, leaf_indices[1:]):
            yield a
