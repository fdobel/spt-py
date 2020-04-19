
"""
This file describes properties of shortest path trees (spt) and the needed operations on spt.
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
...

===Definitions===
Graph G = (V, E).
subgraph: with N \subseteq V : G_{N} = (N, E | N)

Shortest Path Tree w.r.t Graph G: SPT_G(S, T) represents the shortest paths from source nodes S to target node T.

===spts properties===
: single root node R
: each node has zero, one or two children
: for each node and each of its children a weight is stored

1) SPT_G(S, T), S=[s_i|1<=i<=n], target node T the following holds:
2) each leaf (index i) represents a source node (s_i).
3) the accumulated weights from root node to a leaf = distance(s_i, T)

===construction===
= CONSTRUCTION 0
initial: for a graph of a single node n construct a root node that represents the distance of n to itself = 0.
single node graph SN = ({n}, {})
SPT_{SN}({n}, n)= o

= CONSTRUCTION 1
node T'
SPT_G(S, T) ==> SPT_G(S u {T}, T)
---
T is the last element of ordered source nodes.
# todo how is this guaranteed?
existing tree: add root nodes with

= CONSTRUCTION 2
for SPT_G(S, T)
add new node B and single edge e=(T, B) [with b in V \ N],
to G=(V, E)
V'= V u {B}
E'= E u {e}
G':=(V', E') :
    => construction of SPT_G'(S, B) from SPT_G(S, T):
        - existing shortest path tree, add w_{T,B} to both first children of root node.
        # todo - proof correctness.

= CONSTRUCTION 3
add new node B and two edges e1=(T, B), e2=(A, B)

to G=(V, E, w) [with T,A in V]
[assumption : d(A, T) < infinity in G]

    G1'=(V u {B}, E u {e1}), G2' = (V u {B}, E u {e2})

    => construct SPT_G1'(S, B) from  SPT_G(S, T)
    => construct SPT_G2'(S, B) from SPT_G(S, A)
    G'=(V u {B}, E u {e1,e2})
    => construct SPT_G'(S, B) from SPT_G1'(S, B) and SPT_G2'(S, B)
    : needed premises -> S is ordered

    # todo - the following needs to be worked out. be more precise.
    construction as follows: find minimal k, s.t. :
                                        - for all l<k:  all shortest paths from s_l to B go through e1(=(T, B))
                                        - for all l>=k: all shortest paths from s_l to B go through e2(=(A, B))
    split SPT_G1'(S, B) and SPT_G2'(S, B) along path to leaf representing s_l.
    => SPT_G1'(S, B) representing shortest paths through T and e1
    => SPT_G2'(S, B) representing shortest paths through A and e2
    - combine trees along path. [s_k is taken from SPT_G2' as shortest path from s_k is edge case going through e2]
    # todo existance of minimal k found below (§3?)



definitions:
sp(v, w) = (v...w) := shortest path from v to w
sd(v, w) := distance of path sp(v, w)
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

=> ASSUME not exists i,j s.t. a_i = b_j.
    - (p1 T) with distance d_1 + d(t1,T) and (p2 T) with distance d_2 + d(t2, T)
                                will be part of combined shortest path tree.
===§3=== grid graph case
- let source nodes S=[s_1,..., s_n] be ordered such that the following is true
            - for all i,j in |n|, j > i, for all nodes n s.t. n is reachable from s_j, then n is also reachable from s_i

- with §2 the following is true:
    - when constructing a combined shortest path tree:
        - there exists a minimal k s.t. for all i <= k: sp(s_i, T) goes through t1
                                    and for all i > k: sp(s_i, T) goes through t2
            because:
                    => assume exists i,j in |n|, j<i, such that sp(s_j)=p_j' goes through t2 and sp(s_i)=p_i' goes through t1.
                    => p_j' and p_i' intersect => n in p_j' s.t. n in p_i' such that the paths split after n
                    - due to construction as seen in §2, we can construct a shorter path for either p_j' or p_i' -
                    => therefore we could construct a shorter path from s_i that goes through t2 or s_j that goes through t1

        => there is a minimal i such that: for all j > i: d(s_j, s_i) = infinity

===$3===

"""