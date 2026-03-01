class Solution:
    def minimumOR(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0
        valid_mask = 0
        
        for bit in range(30, -1, -1):
            target_mask = valid_mask | (1 << bit)
            possible = True
            
            for i in range(m):
                row_possible = False
                for j in range(n):
                    if (grid[i][j] & target_mask) == 0:
                        row_possible = True
                        break
                if not row_possible:
                    possible = False
                    break
                    
            if not possible:
                ans |= (1 << bit)
            else:
                valid_mask |= (1 << bit)
                
        return ans
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        