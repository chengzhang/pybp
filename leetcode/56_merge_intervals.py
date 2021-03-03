
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
# 提示：
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

import pdb

class Solution(object):
    def merge(self, intervals):
        m = min([it[0] for it in intervals])
        M = max([it[1] for it in intervals])
        flag = [[0, 0] for _ in range(m, M+1)]
        for inter in intervals:
            begin, end = inter
            flag[begin-m][0] += 1
            flag[end-m][1] += 1
        result = []
        begin, stack = None, None
        for i in range(m, M+1):
            if flag[i-m] == [0, 0]:
                continue
            n_begin, n_end = flag[i-m]
            if begin is None:
                begin = i
                stack = n_begin
            else:
                stack += n_begin
            stack -= n_end
            if stack == 0:
                result.append([begin, i])
                begin, stack = None, None
        return result


    def merge_bak(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= result[-1][1]:
                result[-1][1] = max(inter[1], result[-1][1])
            else:
                result.append(inter)
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[1,4],[0,4]], [[0, 4]]),
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
    ]
    for case in test_cases:
        intervals , golden = case
        result = solution.merge(intervals)
        print(result, golden)
        assert result == golden
