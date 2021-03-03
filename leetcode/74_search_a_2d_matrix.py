class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])
        down, up = 0, M
        while down < up:
            row = (down + up) // 2
            value = matrix[row][0]
            if value == target:
                return True
            elif value < target:
                down = row + 1
            else:
                up = row
        if up == 0:
            return False
        row = up - 1
        left, right = 0, N
        while left < right:
            col = (left + right) // 2
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = col + 1
            else:
                right = col
        return False


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ]
    for case in test_cases:
        matrix, target, golden = case
        result = solution.searchMatrix(matrix, target)
        print(result, golden)
        assert result == golden
