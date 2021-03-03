class Node(object):
    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class UnionFindSet(object):
    def __init__(self):
        self.parent = {}
        self.tree_size = {}
        self.n_edge = 0

    # def find(self, node: Node) -> Node:
    def find(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.tree_size[node] = 1
            return node
        father = self.parent[node]
        while father != node:
            grandfather = self.parent[father]
            if grandfather != father:
                self.tree_size[father] -= 1
                self.parent[node] = grandfather
            node = father
            father = grandfather
        return father

    # def union(self, a: Node, b: Node) -> Node:
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return False
        if self.tree_size[a_root] < self.tree_size[b_root]:
            a_root, b_root = b_root, a_root
        self.parent[b_root] = a_root
        self.tree_size[a_root] += self.tree_size[b_root]
        self.n_edge += 1
        return True

    def get_unions(self): # -> List[Set[Node]]:
        root_2_unions = {}
        for node, parent in self.parent.items():
            root = self.find(node)
            if root not in root_2_unions:
                root_2_unions[root] = {node}
            else:
                root_2_unions[root].add(node)
        return list(root_2_unions.values())

    def get_n_edge(self):
        return self.n_edge


class XNode(Node):
    def __init__(self, num):
        self.num = num

    def __hash__(self):
        return self.num


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        result = 0
        alice_set = UnionFindSet()
        bob_set = UnionFindSet()
        for edge in edges:
            t, a, b = edge
            if t != 3:
                continue
            a_node = XNode(a)
            b_node = XNode(b)
            did_union = alice_set.union(a_node, b_node)
            bob_set.union(a_node, b_node)
            if not did_union:
                result += 1
        for edge in edges:
            t, a, b = edge
            if t == 3:
                continue
            a_node = XNode(a)
            b_node = XNode(b)
            if t == 1:
                did_union = alice_set.union(a_node, b_node)
                if not did_union:
                    result += 1
            else:
                did_union = bob_set.union(a_node, b_node)
                if not did_union:
                    result += 1
        if alice_set.get_n_edge() != n - 1:
            return -1
        if bob_set.get_n_edge() != n - 1:
            return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2),
        (4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0),
        (4, [[3,2,3],[1,1,2],[2,3,4]], -1),
    ]
    for case in test_cases:
        n, edges, golden = case
        result = solution.maxNumEdgesToRemove(n, edges)
        print(result, golden)
        assert result == golden
