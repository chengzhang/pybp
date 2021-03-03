# 474. 一和零
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#
# 示例 # 1：
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10", "0001", "1", "0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001", "1"} 和 {"10", "1", "0"} 。
# {"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

# 示例 # 2：
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 # {"0", "1"} ，所以答案是 # 2 。
#
# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[L][M][N]
        L = len(strs) + 1
        M = m + 1
        N = n + 1
        dp = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(L)]
        for i in range(1, L):
            s = strs[i-1]
            cnt0 = len([it for it in s if it == '0'])
            cnt1 = len([it for it in s if it == '1'])
            for j in range(M):
                for k in range(N):
                    no_choose = dp[i-1][j][k]
                    if j >= cnt0 and k >= cnt1:
                        choose = 1 + dp[i-1][j-cnt0][k-cnt1]
                        dp[i][j][k] = max(no_choose, choose)
                    else:
                        dp[i][j][k] = no_choose
        return dp[L-1][m][n]


if __name__ == '__main__':
    test_cases = [
        (["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (["10", "0", "1"], 1, 1, 2),
    ]
    s = Solution()
    for case in test_cases:
        strs, m, n, golden = case
        result = s.findMaxForm(strs, m, n)
        assert result == golden
