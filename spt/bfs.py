

def bfs_tree(node):
    visited = set()  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        yield s

        children = []
        if s.left is not None:
            children.append(s.left.child)
        if s.right is not None:
            children.append(s.right.child)
        for neighbour in children:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
