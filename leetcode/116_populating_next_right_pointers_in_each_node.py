import pdb

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        arr = [root]
        self.bfs(arr)
        return root

    def bfs(self, arr):
        if not arr:
            return
        new_arr = []
        N = len(arr)
        for i, node in enumerate(arr):
            if i == N - 1:
                node.next = None
            else:
                node.next = arr[i+1]
            if node.left:
                new_arr.append(node.left)
                new_arr.append(node.right)
        self.bfs(new_arr)

    def build_tree(self, values):
        def __build_tree(index):
            if index >= len(values):
                return None
            left = 2 * index + 1
            left_node = __build_tree(left)
            right = 2 * index + 2
            right_node = __build_tree(right)
            root = Node(values[index], left=left_node, right=right_node)
            return root
        tree_root = __build_tree(0)
        return tree_root

    def judge(self, next, result):
        nodes = [result]
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            i += 1
        for golden, node in zip(next, nodes):
            if node.next != golden and node.next.val != golden:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], [None, 3, None, 5, 6, 7, None]),
    ]
    for case in test_cases:
        values, next = case
        root = solution.build_tree(values)
        result = solution.connect(root)
        assert solution.judge(next, result)
