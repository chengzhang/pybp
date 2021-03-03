class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        result = []
        over = 0
        i = len(A) - 1
        k = K
        for i in list(range(len(A)))[::-1]:
            a = A[i]
            b = k % 10
            k = k // 10
            s = a + b + over
            over = s // 10
            s = s % 10
            result.append(s)
        while k > 0:
            b = k % 10
            k = k // 10
            s = b + over
            over = s // 10
            s = s % 10
            result.append(s)
        if over:
            result.append(over)
        result = result[::-1]
        return result


if __name__ == '__main__':
    cases = [
        ([1,2,0,0], 34, [1,2,3,4]),
        ([2,7,4], 181, [4,5,5]),
        ([2,1,5], 806, [1,0,2,1]),
        ([9,9,9,9,9,9,9,9,9,9], 1, [1,0,0,0,0,0,0,0,0,0,0]),
    ]
    s = Solution()
    for case in cases:
        A, K, golden = case
        result = s.addToArrayForm(A, K)
        print('golden: {}, result: {}'.format(golden, result))
        assert result == golden
