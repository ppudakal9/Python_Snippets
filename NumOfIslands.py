class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        row = len(grid)
        column = len(grid[0])
        numOfIslands = 0

        for i in range(0, row):
            for j in range(0, column):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    self._convert(grid, i, j)

        return numOfIslands

    def _convert(self, grid, i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0'):
            return

        # else convert land to water i.e. 1 to 0
        grid[i][j] = '0'

        # recursively convert all connected land to water
        self._convert(grid, i - 1, j)
        self._convert(grid, i + 1, j)
        self._convert(grid, i, j - 1)
        self._convert(grid, i, j + 1)


