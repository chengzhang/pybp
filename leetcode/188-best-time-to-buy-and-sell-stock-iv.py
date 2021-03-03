
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        best_one_deal = self.get_best_one_deal(prices)
        dp = [[0 for j in range(k)] for i in range(N)]
        # dp[i][j] == best(prices[0:i], j)
        for i in range(N):
            for j in range(k):
                for x in range(i):
                    dp[i][j] = max(dp[i][j], dp[x][j-1] + best_one_deal[x][i])
                    dp[i][j] = max(dp[i][j], dp[x][j])
        return dp[N-1][k-1]

    def get_best_one_deal(self, prices):
        N = len(prices)
        best_one_deal = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            m, M = prices[i], prices[i]
            for j in range(i+1, N):
                m = min(m, prices[j])
                M = max(M, prices[j])
                best_one_deal[i][j] = M - m


if __name__ == '__main__':
    test_cases = [
        ([2,4,1], 2, 2),
        ([3,2,6,5,0,3], 2, 7),
    ]

    s = Solution()
    for case  in test_cases:
        prices, k, golden = case
        result = s.maxProfit(k, prices)
        assert result == golden
