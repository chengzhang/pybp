class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(matrix)
        N = len(matrix[0])
        result = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                result[i][j] = matrix[j][i]
        return result