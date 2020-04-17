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


def tree_node_to_node(node, leaf_indices):
    node_path = [node]

    next_idx = leaf_indices.pop()

    lu = node
    print(lu)
    for direction in find_leaf(node, next_idx):

        print(direction)
        # next_node = None
        if direction == 'left':
            lu = lu.left.child
            node_path.append(lu)

        if direction == 'right':
            lu = lu.right.child
            node_path.append(lu)

        print(lu)




if __name__ == '__main__':
    b = NodeBuilder()

    m1 = b.mid(
        b.mid(b.leaf("0"), b.leaf("1")),
        b.mid(b.leaf("2"), b.leaf("3"))
    )

    m2 = b.mid(
        b.mid(b.leaf("x0"), b.leaf("x1")),
        b.mid(b.leaf("x2"), b.leaf("x3"))
    )
    tree_node_to_node(m1, [1])

