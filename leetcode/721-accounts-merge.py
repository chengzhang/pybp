from typing import List, Set

class Node(object):
    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class UnionFindSet(object):
    def __init__(self):
        self.parent = {}
        self.tree_size = {}

    def find(self, node: Node) -> Node:
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

    def union(self, a: Node, b: Node) -> Node:
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return a_root
        if self.tree_size[a_root] < self.tree_size[b_root]:
            a_root, b_root = b_root, a_root
        self.parent[b_root] = a_root
        self.tree_size[a_root] += self.tree_size[b_root]
        return a_root

    def get_unions(self) -> List[Set[Node]]:
        root_2_unions = {}
        for node, parent in self.parent.items():
            root = self.find(node)
            if root not in root_2_unions:
                root_2_unions[root] = {node}
            else:
                root_2_unions[root].add(node)
        return list(root_2_unions.values())

class EmailNode(Node):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(self.email)


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_set = UnionFindSet()
        for lst in accounts:
            name = lst[0]
            emails = lst[1:]
            for i, e in enumerate(emails):
                node_i = EmailNode(name, e)
                for e1 in emails[i:]:
                    node_j = EmailNode(name, e1)
                    email_set.union(node_i, node_j)
        subset = email_set.get_unions()
        result = []
        for union in subset:
            name = None
            emails = []
            for node in union:
                name = node.name
                emails.append(node.email)
            emails = sorted(emails)
            result.append([name] + emails)
        return result


def judge_equal(result, golden):
    def __to_set(lst):
        arr = []
        for it in lst:
            s = ';'.join(it)
            arr.append(s)
        return set(arr)
    result_set = __to_set(result)
    golden_set = __to_set(golden)
    chaji = result_set - golden_set
    return not len(chaji)

if __name__ == '__main__':
    test_cases = [
        ([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
         [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]),
    ]
    s = Solution()
    for case in test_cases:
        accounts, golden = case
        result = s.accountsMerge(accounts)
        assert judge_equal(result, golden)
