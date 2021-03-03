# 1124.
# 表现良好的最长时间段
# 给你一份工作时间表hours，上面记录着某一位员工每天的工作小时数。
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格大于「不劳累的天数」。
# 请你返回「表现良好时间段」的最大长度。
#
# 示例 1：
# 输入：hours = [9, 9, 6, 0, 6, 6, 9]
# 输出：3
# 解释：最长的表现良好时间段是[9, 9, 6]。
#
# 提示：
# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16
#

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        result = 0
        stack = []
        for i, h in enumerate(hours):
            if not stack:
                stack.append((i, h))
                continue
            if h > 8:
                if stack[-1][1] > 8:
                    stack.append((i, h))
                else:
                    local_result = i - stack[-1][0]
                    if local_result > result:
                        result = local_result
                    stack.pop()
            else:
                if stack[-1][1] > 8:
                    local_result = i - stack[-1][0]
                    if local_result > result:
                        result = local_result
                    stack.pop()
                else:
                    stack.append((i, h))
        if stack[-1][1] > 8:
            return len(hours)
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([9, 9, 6, 0, 6, 6, 9], 3),
        ([6, 9, 9], 3),
    ]
    for case in test_cases:
        n, golden = case
        result = solution.longestWPI(n)
        print(result, golden)
        assert result == golden
