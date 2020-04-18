
"""
This file describes the needed operations on shortest path trees (spt).
Shortest path trees encode a number of shortest distances between pairs of nodes.
Source nodes are those nodes, which appear as a source node in the shortest distances.
Target nodes are those nodes, which appear as a target node.
For now, the shortest path trees here deal with a target node size of one.
The distances can be queried in log N (N tree nodes).

spts can be <created> (initial action)
spts can be <add weight> (if all shortest paths)
 => if a new edge is added to a (target) node t with respect to which the shortest distances were computed,
    all shortest distances are increased by the corresponding weight.
spts can <add a source node> ... (think about this)

spts need to be combined.
if two trees representing the shortest paths from the same source node set S and
target nodes t1, t2 and another node T with distance d(t1, T)=p, d(t2, T)=q need to be combined:
With following thoughts:
===§1===
- for s1, s2 in S;s1 != s2,
- for any two shortest paths p1=(s1...t), p2=(s2...t)

1. p1 and p2 are disjoint [disregarding t1].
2. let p1=(a_1...a_k), p2=(b_1...b_l). There exists 1<=i<k, 1<=j<l such that for all integer h [s.t. 0 <= h <= k-i]
                                        => a_{i+h} = b_{j+h}
    In other words: without loss of generality we can assume that once any two shortest paths touched a common node,
                    these two paths will follow the same node sequence afterwards.

===§2===
- for s1, s2 in S;s1 != s2,
- for any two shortest paths p1=(s1...t1)=(a_1...a_k) with distance d_1, p2=(s2...t2)=(b_1...b_l) with distance d_2

Task: create a combined shortest path tree representing all shortest paths from S to T
=> Assume there exists i,j such that a_i = b_j. [the two paths intersect]
 ---> assume subpath p1'=(a_i a_{i+1}...t1), distance d_1' and subpath p2'=(b_j...t2) with distance d_2'
    - if d1' + d(t1, T) < d2' + d(t2, T) ; then (p2 T) will not be part of the combined shortest path tree,
                                as we can construct a shorter path for s2 to T being (b_1...b_j a_{i+1} a_k T)
    - if "equal": multiple shortest paths have equal distance
    - if d1 + d(t1, T) > d2 + d(t2, T) ; then p1 will not be part of the combined shortest path tree,
                               as we can construct a shorter path for s1 to T being (a_1...a_i b_{j+1} b_l T)

=> Assume there exists no i,j st a_i = b_j.
    - (p1 T) with distance d_1 + d(t1,T) and (p2 T) with distance d_2 + d(t2, T)
                                will be part of combined shortest path tree.
===§3=== grid graph case
- let source nodes S=[s_1,..., s_n] be ordered such that the following is true
            - for all i: s_i, for all s_j: j > i, d(s_j, s_i) = infinity and d(s_i, s_j) < infinity


"""