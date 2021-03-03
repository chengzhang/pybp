import pdb

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = sum(B)
        diff = sum_a - sum_b
        set_b = set(B)
        for a in A:
            b = a - diff // 2
            if b in set_b:
                return [a, b]


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([1,1], [2,2], [1, 2]),
        ([1,2], [2,3], [1, 2]),
        ([2], [1,3], [2, 3]),
        ([1,2,5], [2,4], [5, 4]),
    ]
    for case in test_cases:
        A, B, golden = case
        result = solution.fairCandySwap(A, B)
        print(result, golden)
        assert result == golden
