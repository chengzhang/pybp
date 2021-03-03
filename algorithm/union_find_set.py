# coding = utf8


class Node(object):
    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__hash__()


class UnionFindSet(object):
    def __init__(self):
        self.parent = {}
        self.tree_size = {}

    def find(self, node):
        """ find the root node which stands for a sub set
        :param node: Node type
        :return: root node, Node type
        """
        if node not in self.parent:
            self.parent[node] = node
            self.tree_size[node] = 1
            return node
        father = self.parent[node]
        while father != node:
            grandfather = self.parent[father]
            if grandfather != father:
                self.parent[node] = grandfather
                self.tree_size[father] -= 1
            node = father
            father = grandfather
        return father

    def union(self, a, b):  # Node type
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return root_a
        if self.tree_size[root_a] < self.tree_size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.tree_size[root_a] += self.tree_size[root_b]
        return root_a

    def get_unions(self):
        unions = {}
        for node, parent in self.parent.items():
            root = self.find(node)
            if root not in unions:
                unions[root] = {node}
            else:
                unions[root].add(node)
        return unions
