# 面试题 16.19. 水域大小
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。
# 由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。
# 编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
#
# 示例：
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]

# 提示：
# 0 < len(land) <= 1000
# 0 < len(land[i]) <= 1000

import pdb


class Solution(object):
    def pondSizes(self, land):
        result = []
        for i, row in enumerate(land):
            for j, value in enumerate(row):
                num = self.dfs(land, i, j)
                if num:
                    result.append(num)
        return sorted(result)

    def dfs(self, land, i, j):
        if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] != 0:
            return 0
        land[i][j] = 1
        num = 1
        num += self.dfs(land, i-1, j-1)
        num += self.dfs(land, i-1, j)
        num += self.dfs(land, i-1, j+1)
        num += self.dfs(land, i,   j-1)
        num += self.dfs(land, i,   j+1)
        num += self.dfs(land, i+1, j-1)
        num += self.dfs(land, i+1, j)
        num += self.dfs(land, i+1, j+1)
        return num


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([
             [0,2,1,0],
             [0,1,0,1],
             [1,1,0,1],
             [0,1,0,1]
         ],
         [1,2,4]
        ),
    ]
    for case in test_cases:
        land, golden = case
        result = solution.pondSizes(land)
        assert result == golden
