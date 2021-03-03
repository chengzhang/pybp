# 307. 区域和检索 - 数组可修改
# 给你一个数组 nums ，请你完成两类查询，其中一类查询要求更新数组下标对应的值，另一类查询要求返回数组中某个范围内元素的总和。
#
# 实现 NumArray 类：
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值更新为 val
# int sumRange(int left, int right) 返回子数组 nums[left, right] 的总和（即，nums[left] + nums[left + 1], ..., nums[right]）
#
# 示例：
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
#
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 9 ，sum([1, 3, 5]) = 9
# numArray.update(1, 2); // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // 返回 8 ，sum([1, 2, 5]) = 9
#
# 提示：
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 最多调用 3 * 104 次 update 和 sumRange 方法
#
# 通过次数17, 729 提交次数30, 941


class TreeNode(object):
    def __init__(self, begin, end, s, left=None, right=None):
        self.begin = begin
        self.end = end
        self.sum = s
        self.left_son = left
        self.right_son = right

class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.root = self._build_segment(0, len(nums) - 1)

    def _build_segment(self, begin, end):
        if begin != end:
            mid = (begin + end) // 2
            left_son = self._build_segment(begin, mid)
            right_son = self._build_segment(mid+1, end)
            node = TreeNode(begin, end, left_son.sum + right_son.sum, left_son, right_son)
        else:
            node = TreeNode(begin, end, self.nums[begin])
        return node

    def sum_range(self, begin, end):
        return self._sum_range_on_node(self.root, begin, end)

    def _sum_range_on_node(self, node, begin, end):
        if node.begin == begin and node.end == end:
            return node.sum
        if node.right_son.begin > end:  # totally on left son
            return self._sum_range_on_node(node.left_son, begin, end)
        if node.left_son.end < begin:  # totally on right son
            return self._sum_range_on_node(node.right_son, begin, end)
        left_s = self._sum_range_on_node(node.left_son, begin, node.left_son.end)
        right_s = self._sum_range_on_node(node.right_son, node.right_son.begin, end)
        return left_s + right_s

    def update(self, index, value):
        sum_increase = value - self.nums[index]
        self.nums[index] = value
        self._update_on_node(self.root, index, sum_increase)

    def _update_on_node(self, node, index, sum_increase):
        node.sum += sum_increase
        if node.begin == node.end == index:
            return
        if index <= node.left_son.end:
            self._update_on_node(node.left_son, index, sum_increase)
        else:
            self._update_on_node(node.right_son, index, sum_increase)


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = SegmentTree(nums)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.tree.update(index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.tree.sum_range(left, right)


if __name__ == '__main__':
    test_cases = [
        (["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]], [None, 9, None, 8]),
    ]
    na = NumArray([1, 3, 5])
    assert na.sumRange(0, 2) == 9
    na.update(1, 2)
    assert na.sumRange(0, 2) == 8


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


