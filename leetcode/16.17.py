# 面试题 16.17. 连续数列
# 给定一个整数数组，找出总和最大的连续数列，并返回总和。
#
# 示例：
# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶：
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. empty result or non empty result? non empty
        result = nums[0]
        dp = 0
        for i, val in enumerate(nums):
            if dp > 0:
                dp += val
            else:
                dp = val
            if dp > result:
                result = dp
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ]
    for case in test_cases:
        nums, golden = case
        result = solution.maxSubArray(nums)
        print(result, golden)
        assert result == golden
