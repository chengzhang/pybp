class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        if len(s) < 2:
            return 0
        prv, now = 0, 1
        result = 0
        while now < len(s):
            if s[prv] != s[now]:
                prv, now = now, now + 1
                continue
            if cost[prv] < cost[now]:
                result += cost[prv]
                prv, now = now, now + 1
            else:
                result += cost[now]
                now = now + 1
        return result


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ("abaac", [1,2,3,4,5], 3),
        ("abc", [1,2,3], 0),
        ("aabaa", [1,2,3,4,1], 2),
    ]
    for case in test_cases:
        s, cost, golden = case
        result = solution.minCost(s, cost)
        print(result, golden)
        assert result == golden