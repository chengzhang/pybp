
class SegmentTree(object):
    def __init__(self, lb, ub):
        self.lb = lb  # seg tree 一定有一个下界
        self.ub = ub  # 一定有一个上界
        n = ub - lb  # n 一定要足够小。如果n的范围是整个int范围，那seg tree并不合适, 因为seg tree 有 大约 2n 个节点
        self.seg_nodes = [0] * 2 * n  # 2n 的估算方法是，叶子结点 n 个， 再上一层 n/2 个，依次类推. 左右子节点平分父节点的区间. 一开始就建好了整棵树结构。

    def update(self, x):
        def _update(node, begin, end):
            if end <= begin:
                return
            if x < begin or x >= end:
                return
            self.seg_nodes[node] += 1
            mid = (begin + end) // 2
            _update(node*2+1, begin, mid)
            _update(node*2+2, mid+1, end)
        _update(0, self.lb, self.ub)

    def query(self, left, right):
        def _query(node, begin, end):
            if end <= begin:
                return 0
            if end <= left or right <= begin:
                return 0
            if left <= begin and end <= right:
                return self.seg_nodes[node]
            mid = (begin + end) // 2
            return _query(node*2+1, begin, mid) + _query(node*2+2, mid+1, end)  # 左右子节点的运算要符合可加性
        return _query(0, self.lb, self.ub)


# 1649. 通过指令创建有序数组
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        tree = SegmentTree(1, 100001)
        result = 0
        for val in instructions[1:]:
            n_lt = tree.query(1, val)
            n_gt = tree.query(val+1, 100001)
            result += min(n_lt, n_gt)
            tree.update(val)
        return result