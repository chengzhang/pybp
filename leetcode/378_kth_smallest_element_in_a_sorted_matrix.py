# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

import pdb

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low, high = matrix[0][0], matrix[-1][-1] + 1
        while low < high:
            mid = (low + high) // 2
            order, cnt = self.find_x_order(matrix, mid)
            if cnt == 0:
                if k - 1 < order:
                    high = mid
                else:
                    low = mid + 1
            else:
                if k - 1 < order:
                    high = mid
                elif k - 1 < order + cnt:
                    return mid
                else:
                    low = mid + 1

    def find_x_order(self, matrix, x):
        N = len(matrix)
        order = 0
        cnt = 0
        begin_col = 0
        for row in range(N-1, -1, -1):
            insert_index, exist = self.find_insert_index(matrix, x, row, begin_col, N)
            # if x == 13:
            #     print('row {}, begin_col {}, insert {}, exist {}'.format(row, begin_col, insert_index, exist))
            #     pdb.set_trace()
            if exist:
                first_x = self.find_first(matrix, x, row, begin_col, insert_index)
                last_x = self.find_last(matrix, x, row, insert_index, N)
                begin_col = first_x
                cnt += last_x - first_x + 1
            else:
                begin_col = insert_index
            order += begin_col
        return order, cnt

    def find_insert_index(self, matrix, x, row, begin_col, end_col):
        while begin_col < end_col:
            mid = (begin_col + end_col) // 2
            if matrix[row][mid] < x:
                begin_col = mid + 1
            elif matrix[row][mid] == x:
                return mid, True
            else:
                end_col = mid
        return end_col, False

    def find_first(self, matrix, x, row, begin, end):
        """initially, matrix[row][end] == x"""
        while begin < end:
            mid = (begin + end) // 2
            if matrix[row][mid] != x:
                begin = mid + 1
            else:
                end = mid
        return end

    def find_last(self, matrix, x, row, begin, end):
        """initially, matrix[row][begin] == x"""
        while begin < end:
            mid = (begin + end) // 2
            if mid == begin:
                break
            if matrix[row][mid] != x:
                end = mid - 1
            else:
                begin = mid
        return begin


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]
            ],
            8, 13
        ),
    ]
    for case in test_cases:
        matrix, k, golden = case
        result = solution.kthSmallest(matrix, k)
        print(result, golden)
        assert result == golden
