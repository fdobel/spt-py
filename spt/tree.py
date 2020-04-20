from spt.bfs import bfs_tree


class _Edge:
    def __init__(self, parent, child: "_Node", weight):
        self._parent = parent
        self._child = child
        self._weight = weight

    @property
    def child(self):
        return self._child

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return "e(%s)=>[%s]" %(str(self._weight), str(self._child))


class _Node:
    def __init__(self, name="", depth=None, leaf_nodes=None):
        self._left_edge : _Edge = None
        self._right_edge : _Edge = None
        self.name = name
        self._depth = depth

        self._leaf_nodes = leaf_nodes

        if name == "":
            self.name = "o"

    @property
    def leaf_nodes(self):
        return self._leaf_nodes

    @property
    def is_leaf(self):
        return self.left is None and self.left is None

    @property
    def depth(self):
        return self._depth

    @property
    def left(self) -> _Edge:
        return self._left_edge

    @property
    def right(self) -> _Edge:
        return self._right_edge
  
    def _set_left_edge(self, left_edge: _Edge):
        self._left_edge = left_edge
  
    def _set_right_edge(self, right_edge: _Edge):
        self._right_edge = right_edge

    def bfs(self):
        n: _Node
        print("A")
        for n in bfs_tree(self):
            print("Node:", n.name)

    def __str__(self):
        if self._left_edge is None and self._right_edge is None:
            return "<%s>" % str(self.name)
        return "N:[%s]-%s-[%s]" % (str(self._left_edge), str(self.name), str(self._right_edge))
  
    def replace_left_edge(self, new_left: "_Node", new_left_weight: float):
        n = _Node()
        re = self.right
        n._set_right_edge(_Edge(n, re.child, re.weight))
        n._set_left_edge(_Edge(n, new_left, new_left_weight))
        return n

    def replace_right_edge(self, new_right: "_Node", new_right_weight: float):
        n = _Node()
        re = self.left
        n._set_right_edge(_Edge(n, new_right, new_right_weight))
        n._set_left_edge(_Edge(n, re.child, re.weight))
        return n

    def _get_nodes_at_depth(self, depth):
        if depth <= 0:
            yield self
        else:
            for f in self._left_edge.child._get_nodes_at_depth(depth - 1):
                yield f


class NodeBuilder:
    def __init__(self):
        pass

    def leaf(self, name):
        return _Node(name=name, depth=0, leaf_nodes=[name])

    def only_left_child(self, left_node, lw=0):
        ld = left_node.depth if left_node is not None else 0
        depth = ld + 1
        ll = left_node.leaf_nodes if left_node is not None else []

        n = _Node(depth=depth, leaf_nodes=ll)
        n._set_left_edge(_Edge(n, left_node, lw))
        return n

    def mid(self, left_node, right_node, lw=0, rw=0):
        ld = left_node.depth if left_node is not None else 0
        rd = right_node.depth if right_node is not None else 0

        depth = max(ld, rd) + 1
        ll = left_node.leaf_nodes if left_node is not None else []
        rl = right_node.leaf_nodes if right_node is not None else []
        n = _Node(depth=depth, leaf_nodes=ll + rl)
        n._set_left_edge(_Edge(n, left_node, lw))
        n._set_right_edge(_Edge(n, right_node, rw))
        return n

