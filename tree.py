

class Edge:
  def __init__(self, parent, child, weight):
    self._parent = parent
    self._child = child
    self._weight = weight

class Node:
  def __init__(self, left, right):
    self._left = left
    self._right = right

