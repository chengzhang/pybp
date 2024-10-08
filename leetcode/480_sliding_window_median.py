# 480. 滑动窗口中位数
# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
#
# 例如：
# [2,3,4]，中位数是 3
# [2,3]，中位数是 (2 + 3) / 2 = 2.5
# 给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
#
# 示例：
#
# 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
#
# 窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7      -1
#  1  3 [-1  -3  5] 3  6  7      -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
#  因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
#
# 提示：
# 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
# 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。

import heapq
import pdb

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        result = []
        left_mid, right_mid = self.get_mid_index(k)
        win = sorted(nums[:k])
        result.append((win[left_mid] + win[right_mid]) / 2)
        for i, num in enumerate(nums[k:]):
            win_begin = i
            win_end = i + k
            if nums[win_begin] < win[left_mid] and num <= win[left_mid]:
                result.append((win[left_mid] + win[right_mid]) / 2)
                continue
            if win[right_mid] < nums[win_begin] and win[right_mid] < num:
                result.append((win[left_mid] + win[right_mid]) / 2)
                continue
            win = sorted(nums[win_begin+1:win_end+1])
            result.append((win[left_mid] + win[right_mid]) / 2)
        return result

    def get_mid_index(self, k):
        if k % 2 == 0:
            left_mid = k // 2 - 1
            right_mid = left_mid + 1
        else:
            left_mid = k // 2
            right_mid = left_mid
        return left_mid, right_mid


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1,4,2,3], 4, [2.5]),
        ([1,3,-1,-3,5,3,6,7], 3, [1,-1,-1,3,5,6]),
    ]
    for case in test_cases:
        nums, k, golden = case
        result = solution.medianSlidingWindow(nums, k)
        print(result, golden)
        assert result == golden

# 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
