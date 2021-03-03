class Node(object):
    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class UnionFindSet(object):
    def __init__(self):
        self.parent = {}
        self.tree_size = {}

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
            return a_root
        if self.tree_size[a_root] < self.tree_size[b_root]:
            a_root, b_root = b_root, a_root
        self.parent[b_root] = a_root
        self.tree_size[a_root] += self.tree_size[b_root]
        return a_root

    def get_unions(self): # -> List[Set[Node]]:
        root_2_unions = {}
        for node, parent in self.parent.items():
            root = self.find(node)
            if root not in root_2_unions:
                root_2_unions[root] = {node}
            else:
                root_2_unions[root].add(node)
        return list(root_2_unions.values())
