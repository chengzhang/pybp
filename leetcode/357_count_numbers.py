#  357. 计算各个位数不同的数字个数
#  给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
#
#  示例:
#
#  输入: 2
#  输出: 91
#  解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        result = 10
        base = 9
        multi = 9
        for i in range(2, n+1):
            base = base * multi
            multi -= 1
            result += base
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (0, 1),
        (1, 10),
        (2, 91),
    ]
    for case in test_cases:
        n, golden = case
        result = solution.countNumbersWithUniqueDigits(n)
        print(result, golden)
        assert result == golden


