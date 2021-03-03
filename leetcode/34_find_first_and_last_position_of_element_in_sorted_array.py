import pdb


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = -1, -1
        begin, end = 0, len(nums) - 1
        while begin < len(nums) and end > -1 and begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                left = self.find_left_bound(nums, mid)
                right = self.find_right_bound(nums, mid)
                break
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1
        return [left, right]

    def find_left_bound(self, nums, bound):
        left = 0
        while left < bound:
            mid = (left + bound) // 2
            if nums[mid] == nums[bound]:
                bound = mid
            else:
                left = mid + 1
        return bound

    def find_right_bound(self, nums, bound):
        right = len(nums) - 1
        while bound < right:
            mid = (bound + right + 1) // 2
            if nums[mid] == nums[bound]:
                bound = mid
            else:
                right = mid - 1
        return bound


if __name__ == '__main__':
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5,7,7,8,8,10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ]
    s = Solution()
    for case in test_cases:
        nums, target, golden = case
        result = s.searchRange(nums, target)
        #pdb.set_trace()
        assert result == golden
