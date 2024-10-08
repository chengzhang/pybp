# 面试题 16.11. 跳水板
# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。
#
# 示例 1
#
# 输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： [3,4,5,6]
# 解释：
# 可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。
# 提示：
#
# 0 < shorter <= longer
# 0 <= k <= 100000
# 通过次数44,467提交次数100,655
#

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        lo, hi = shorter * k, longer * k
        result = {lo}
        for length in range(lo+shorter, hi+1):
            x = length - shorter
            if x in result:
                result.add(length)
                continue
            y = length - longer
            if y in result:
                result.add(length)
        return list(result)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (1, 2, 3, [3, 4, 5, 6])
    ]
    for case in test_cases:
        shorter, longer, k, golden = case
        result = solution.divingBoard(shorter, longer, k)
        print(result, golden)
        assert result == golden
