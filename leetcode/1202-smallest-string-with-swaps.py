class UnionFindSet(object):
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        """使用递归的方式来查找父节点

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        father = self.father_dict[node]
        if(node != father):
            if father != self.father_dict[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

    def groups(self):
        root_2_group = {}
        for k, _ in self.father_dict.items():
            root = self.find(k)
            if root not in root_2_group:
                root_2_group[root] = {k, root}
            else:
                root_2_group[root].add(k)
        return list(root_2_group.values())


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graphs = self.sub_graphs(pairs)
        out_s = s
        for g in graphs:
            out_s = self.rearrange(out_s, g)
        return out_s

    def sub_graphs(self, pairs):
        nodes = set()
        for a, b in pairs:
            nodes.add(a)
            nodes.add(b)
        uf_set = UnionFindSet(nodes)
        for a, b in pairs:
            uf_set.union(a, b)
        graphs = uf_set.groups()
        return graphs


    def sub_graphs_0(self, pairs):
        idx_2_graph = {}

        # def __combine(x, y, z):
        #     g = x | y | z
        #     for idx in g:
        #         idx_2_graph[idx] = g

        def __combine2(x, y):
            g = x | y
            for idx in g:
                idx_2_graph[idx] = g

        def __add(x, y):
            gx = idx_2_graph[x]
            gx.add(y)
            idx_2_graph[y] = gx

        def __new(x, y):
            g = {x, y}
            idx_2_graph[x] = g
            idx_2_graph[y] = g

        for a, b in pairs:
            if a in idx_2_graph:
                ga = idx_2_graph[a]
                if b in idx_2_graph:
                    gb = idx_2_graph[b]
                    if ga is gb:
                        pass
                    else:
                        __combine2(ga, gb)
                else:
                    __add(a, b)
            else:
                if b in idx_2_graph:
                    __add(b, a)
                else:
                    __new(a, b)

            # graph = {a, b}
            # a_graph = idx_2_graph[a] if a in idx_2_graph else set()
            # b_graph = idx_2_graph[b] if b in idx_2_graph else set()
            # __combine(graph, a_graph, b_graph)

        graphs, ids = [], set()
        for idx, g in idx_2_graph.items():
            if id(g) not in ids:
                graphs.append(g)
                ids.add(id(g))

        return list(graphs)

    def rearrange(self, string, graph):
        indexes = sorted(list(graph))
        chars = [string[i] for i in graph]
        chars = sorted(chars)
        out_chars = list(string)
        for i, c in zip(indexes, chars):
            out_chars[i] = c
        out_string = ''.join(out_chars)
        return out_string


if __name__ == '__main__':
    test_cases = [
        ("dcab", [[0, 3], [1, 2]], "bacd"),
        ("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
        ("cba", [[0, 1], [1, 2]], "abc"),
    ]

    s = Solution()
    for case  in test_cases:
        string, pairs, golden = case
        result = s.smallestStringWithSwaps(string, pairs)
        assert result == golden
