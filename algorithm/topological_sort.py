from typing import List, Optional
from queue import Queue

def topological_sort(adj: List[List[int]], n: int) -> Optional[List[int]]:
    """
    :param adj: adj matrix, adj[i][j] = 1 if j depends on i
    :param n: number of keys, and key belongs to [0, n)
    :return: topo sorted keys
    """
    in_degrees = get_in_degrees(adj, n)
    zero_in_degree_nodes = Queue()
    for i, in_degree in enumerate(in_degrees):
        if not in_degree:
            zero_in_degree_nodes.put(i)
    result = []
    while not zero_in_degree_nodes.empty():
        node = zero_in_degree_nodes.get()
        result.append(node)
        for next, depend in enumerate(adj[node]):
            if depend:
                in_degrees[next] -= 1
                if not in_degrees[next]:
                    zero_in_degree_nodes.put(next)
    if len(result) == n:
        return result
    else:
        return None


def get_in_degrees(adj: List[List[int]], n: int) -> List[int]:
    result = [0] * n
    for i, row in enumerate(adj):
        for j, val in enumerate(row):
            if val:
                result[j] += 1
    return result
