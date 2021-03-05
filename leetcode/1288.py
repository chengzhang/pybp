# 1288. 删除被覆盖区间
# 给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
#
# 只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
#
# 在完成所有删除操作后，请你返回列表中剩余区间的数目。
#
#
#
# 示例：
#
# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
#
#
# 提示：​​​​​​
#
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# 对于所有的 i != j：intervals[i] != intervals[j]
# 通过次数7,914提交次数14,125
#

import pdb

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n_covered = 0
        intervals.sort(key=lambda x: x[0])
        p1, p2 = 0, 0
        max_end = 0
        #pdb.set_trace()
        while p1 < len(intervals):
            while p2 < len(intervals) and intervals[p1][0] == intervals[p2][0]:
                p2 += 1
            same_begin_sorted = sorted(intervals[p1:p2], key=lambda x: x[1], reverse=True)
            if same_begin_sorted[0][1] <= max_end:
                n_covered += p2 - p1
            else:
                n_covered += p2 - p1 - 1
                max_end = same_begin_sorted[0][1]
            p1 = p2
        return len(intervals) - n_covered


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[1,4],[3,6],[2,8]], 2),
        ([[1,2],[1,4],[3,4]], 1),
    ]
    for case in test_cases:
        intervals, golden = case
        result = solution.removeCoveredIntervals(intervals)
        print(result, golden)
        assert result == golden


