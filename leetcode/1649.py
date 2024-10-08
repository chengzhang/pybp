# 1649. 通过指令创建有序数组
# 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。
# 每一次插入操作的 代价 是以下两者的 较小值 ：
#
# nums 中 严格小于  instructions[i] 的数字数目。
# nums 中 严格大于  instructions[i] 的数字数目。
# 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。
#
# 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：instructions = [1,5,6,2]
# 输出：1
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
# 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
# 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
# 总代价为 0 + 0 + 0 + 1 = 1 。
# 示例 2:
#
# 输入：instructions = [1,2,3,6,5,4]
# 输出：3
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
# 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
# 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
# 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
# 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
# 示例 3：
#
# 输入：instructions = [1,3,3,3,2,4,2,1,2]
# 输出：4
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
# 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
# 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
# ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
# 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
# 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
#
#
# 提示：
#
# 1 <= instructions.length <= 105
# 1 <= instructions[i] <= 105


class TreeNode(object):
    def __init__(self, val, cnt=1, left_son=None, right_son=None):
        self.val = val
        self.cnt = cnt
        self.total = cnt
        self.left_son = left_son
        self.right_son = right_son


class BinTree(object):
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def insert(self, val):
        n_lt, n_gt = self._insert(self.root, val)
        return min(n_lt, n_gt)

    def _insert(self, node, val):
        if node.val == val:
            node.cnt += 1
            n_lt = node.left_son.total if node.left_son else 0
            n_gt = node.right_son.total if node.right_son else 0
        elif node.val < val:
            if not node.right_son:
                node.right_son = TreeNode(val, cnt=0)
            n_lt_left = node.left_son.total if node.left_son else 0
            n_lt_right, n_gt = self._insert(node.right_son, val)
            n_lt = n_lt_left + node.cnt + n_lt_right
        else:
            if not node.left_son:
                node.left_son = TreeNode(val, cnt=0)
            n_lt, n_gt_left= self._insert(node.left_son, val)
            n_gt_right = node.right_son.total if node.right_son else 0
            n_gt = n_gt_left + node.cnt + n_gt_right
        node.total += 1
        return n_lt, n_gt


class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        tree = BinTree(instructions[0])
        result = 0
        for val in instructions[1:]:
            result += tree.insert(val)
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1,5,6,2], 1),
        ([1,2,3,6,5,4], 3),
        ([1,3,3,3,2,4,2,1,2], 4),
    ]
    for case in test_cases:
        nums, golden = case
        result = solution.createSortedArray(nums)
        print(result, golden)
        assert result == golden

