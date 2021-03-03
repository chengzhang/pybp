
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        domino_2_cnt = [0] * 91
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            domino = a * 9 + b
            domino_2_cnt[domino] += 1
        n_pair = 0
        for cnt in domino_2_cnt:
            n_pair += cnt * (cnt-1) // 2
        return n_pair

    def num_pair(self, cnt):
        return cnt * (cnt-1) // 2


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[1,2],[2,1],[3,4],[5,6]], 1),
    ]
    for case in test_cases:
        dominoes, golden = case
        result = solution.numEquivDominoPairs(dominoes)
        print(result, golden)
        assert result == golden
