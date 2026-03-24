class Solution(object):
    def constructProductMatrix(self, grid):
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        # flatten
        arr = []
        for row in grid:
            for val in row:
                arr.append(val % MOD)
        
        size = len(arr)
        
        # prefix
        prefix = [1]*size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # suffix
        suffix = [1]*size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # result
        res = [0]*size
        for i in range(size):
            res[i] = (prefix[i] * suffix[i]) % MOD
        
        # reshape to matrix
        ans = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(res[idx])
                idx += 1
            ans.append(row)
        
        return ans
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        