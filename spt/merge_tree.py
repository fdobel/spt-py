from typing import List

from spt.tree import _Node, NodeBuilder


class MergeInfo:
    def __init__(self, direction, new_left_weight, new_right_weight):
        if direction not in ['left', 'right']:
            raise AttributeError("unknown direction")
        self._direction = direction
        self._new_left_weight = new_left_weight
        self._new_right_weight = new_right_weight

    @property
    def dir(self):
        return self._direction

    @property
    def lw(self):
        return self._new_left_weight

    @property
    def rw(self):
        return self._new_right_weight


def merge_binary_tree_along_path_to_leaf(merge_l: _Node, merge_r: _Node, merge_path: List[MergeInfo], pref='left'):
    b = NodeBuilder()

    if len(merge_path) == 0:
        if pref == 'left':
            return merge_l
        return merge_r

    next_mi = merge_path[0]

    if next_mi.dir == 'left':
        return b.mid(
            merge_binary_tree_along_path_to_leaf(
                merge_l.left.child,
                merge_r.left.child,
                merge_path[1:], pref=pref
            ),
            merge_r.right.child, lw=42.0, rw=42.0
        )

    if next_mi.dir == 'right':
        return b.mid(
            merge_l.left.child,
            merge_binary_tree_along_path_to_leaf(
                merge_l.right.child,
                merge_r.right.child,
                merge_path[1:], pref=pref
            ),
            lw=43.0, rw=43.0
        )
    raise RuntimeError()


