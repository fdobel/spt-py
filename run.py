from factories import grid_graph
from shortest_paths import ShortestPaths


def grid_graph_reachable(s, t):
    if s[0] > t[0] or s[1] > t[1]:
        return False
    return True


def log(s):
    if False:
        print(s)


def compute_shortest_paths(gg, s_nodes, t_nodes):
    sp = ShortestPaths(s_nodes, t_nodes)

    for n, oue, ine in gg:

        log("---")
        log("Compute for node: %s" % str(n))

        reachable_from = lambda x: grid_graph_reachable(x, n)

        relevant_source_nodes = list(filter(reachable_from, s_nodes))

        log("Relevant source nodes: %s" % str(relevant_source_nodes))

        for sn_ in relevant_source_nodes:
            if sn_ == n:
                sp.set(sn_, n, 0.0)
                continue
            log("Find shortest path for %s -> %s from known input values" % (str(sn_), str(n)))

            min_value = 24e33
            min_value_node = None
            for inp_node, weight in ine:

                if not grid_graph_reachable(sn_, inp_node):
                    continue
                comb_weight = sp.dist(sn_, inp_node) + weight
                log("    | weight: %s, sp-weight: %s, comb: %s" %
                      (str(weight), str(sp.dist(sn_, inp_node)), str(comb_weight))
                  )

                if min_value > comb_weight:
                    min_value = comb_weight
                    min_value_node = inp_node

            log("SUCCESS - Shortest path %s -> %s = %s" % (str(sn_), str(n), str(min_value)))
            sp.set(sn_, n, min_value)
    return sp

if __name__ == '__main__':

    print(grid_graph)

    source_nodes = [(0, i) for i in range(7)]
    target_nodes = [(2, 6)]

    sp = compute_shortest_paths(grid_graph, source_nodes, target_nodes)
    print(sp)
