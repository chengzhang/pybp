class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_2_index = dict((n, i) for i, n in enumerate(nums))
        for i, n in enumerate(nums):
            m = target - n
            if m in num_2_index:
                return [i, num_2_index[m]]


if __name__ == '__main__':
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
    ]

    s = Solution()
    for case  in test_cases:
        nums, target, golden = case
        result = s.twoSum(nums, target)
        assert result == golden
