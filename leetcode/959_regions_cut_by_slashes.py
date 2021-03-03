# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        M = 4 * N
        new_grid = [[0 for _ in range(M)] for _ in range(M)]
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == '\\':
                    new_grid[4*i+0][4*j+0] = 1
                    new_grid[4*i+1][4*j+1] = 1
                    new_grid[4*i+2][4*j+2] = 1
                    new_grid[4*i+3][4*j+3] = 1
                elif value == '/':
                    new_grid[4*i+0][4*j+3] = 1
                    new_grid[4*i+1][4*j+2] = 1
                    new_grid[4*i+2][4*j+1] = 1
                    new_grid[4*i+3][4*j+0] = 1
        n_region = 0
        for i, row in enumerate(new_grid):
            for j, value in enumerate(row):
                if value == 0:
                    n_region += 1
                    self.dfs(new_grid, i, j)
        return n_region

    def dfs(self, new_grid, i, j):
        M = len(new_grid)
        if i < 0 or i >= M or j < 0 or j >= M or new_grid[i][j] == 1:
            return
        new_grid[i][j] = 1
        self.dfs(new_grid, i-1, j)
        self.dfs(new_grid, i,   j-1)
        self.dfs(new_grid, i,   j+1)
        self.dfs(new_grid, i+1, j)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        ([
            " /",
            "/ "
        ], 2),
        ([
            " /",
            "  "
        ], 1),
        ([
            "\\/",
            "/\\"
        ], 4),
        ([
            "/\\",
            "\\/"
        ], 5),
        ([
            "//",
            "/ "
        ], 3),
    ]
    for case in test_cases:
        grid, golden = case
        result = solution.regionsBySlashes(grid)
        print(result, golden)
        assert result == golden
