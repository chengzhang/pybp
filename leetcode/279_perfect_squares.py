# 279. 完全平方数
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

import pdb

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_square = lambda x: int(x**0.5)**2 == x
        if is_square(n):
            return 1
        for i in range(1, n // 2 + 1):
            j = n - i
            if is_square(i) and is_square(j):
                return 2
        x = n
        while x % 4 == 0:
            x = x // 4
        if x % 8 == 7:
            return 4
        return 3

    def numSquares_bak(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = set()
        for i in range(1, n):
            s = i * i
            if s > n:
                break
            squares.add(s)
        N = n + 1
        dp = [i for i in range(N)]
        for i in range(1, N):
            if i in squares:
                dp[i] = 1
                continue
            for j in range(1, i // 2 + 1):
                k = i - j
                if dp[j] + dp[k] < dp[i]:
                    dp[i] = dp[j] + dp[k]
                    if dp[i] == 2:
                        break
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (12, 3),
        (13, 2),
    ]
    for case in test_cases:
        n, golden = case
        result = solution.numSquares(n)
        print(n, result)
        assert result == golden
