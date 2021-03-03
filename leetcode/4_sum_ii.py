from collections import Counter

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_sum_cnt = self.sum_cnt(A, B)
        cd_sum_cnt = self.sum_cnt(C, D)
        total = sum([0] + [cnt * cd_sum_cnt[-s] for s, cnt in ab_sum_cnt.items() if -s in cd_sum_cnt])
        return total

    def sum_cnt(self, A, B):
        counter = Counter()
        for i in A:
            for j in B:
                s = i + j
                counter.update([s])
        return dict(counter.most_common())


if __name__ == '__main__':
    test_cases = [
        ([1, 2], [-2,-1], [-1, 2], [ 0, 2], 2),
    ]

    s = Solution()
    for case in test_cases:
        A, B, C, D, golden = case
        result = s.fourSumCount(A, B, C, D)
        assert result == golden
