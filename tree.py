

class _Edge:
    def __init__(self, parent, child, weight):
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
        return "<e-%s->:%s>" %(str(self._weight), str(self._child))


class _Node:
    def __init__(self, name=""):
        self._left_edge = None # left_edge
        self._right_edge = None # right_edge
        self.name = name

    @property
    def left(self) -> _Edge:
        return self._left_edge
    @property
    def right(self) -> _Edge:
        return self._right_edge
  
    def _set_left_edge(self, left_edge):
        self._left_edge = left_edge
  
    def _set_right_edge(self, right_edge):
        self._right_edge = right_edge

    def __str__(self):
        if self._left_edge is None and self._right_edge is None:
            return "<%s>" % str(self.name)
        return "<%s - %s - %s>" % (str(self._left_edge), str(self.name), str(self._right_edge))
  
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


class NodeBuilder:
    def __init__(self):
        pass

    def leaf(self, name):
        return _Node(name=name)

    def mid(self, left_node, right_node, lw=0, rw=0):
        n = _Node()
        n._set_left_edge(_Edge(n, left_node, lw))
        n._set_right_edge(_Edge(n, right_node, rw))
        return n

