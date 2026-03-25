class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        # Check horizontal cut
        top_sum = 0
        for i in range(m - 1):  # must leave bottom non-empty
            top_sum += sum(grid[i])
            if top_sum * 2 == total:
                return True
        
        # Check vertical cut
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        left_sum = 0
        for j in range(n - 1):  # must leave right non-empty
            left_sum += col_sums[j]
            if left_sum * 2 == total:
                return True
        
        return False
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        