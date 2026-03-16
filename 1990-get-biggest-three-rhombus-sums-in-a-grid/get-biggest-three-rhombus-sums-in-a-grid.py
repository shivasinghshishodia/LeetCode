class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
                
                # size 0 rhombus
                sums.add(grid[i][j])
                
                size = 1
                while True:
                    if i + 2*size >= m or j - size < 0 or j + size >= n:
                        break
                    
                    total = 0
                    
                    # top -> left
                    r, c = i, j
                    for _ in range(size):
                        total += grid[r][c]
                        r += 1
                        c -= 1
                    
                    # left -> bottom
                    for _ in range(size):
                        total += grid[r][c]
                        r += 1
                        c += 1
                    
                    # bottom -> right
                    for _ in range(size):
                        total += grid[r][c]
                        r -= 1
                        c += 1
                    
                    # right -> top
                    for _ in range(size):
                        total += grid[r][c]
                        r -= 1
                        c -= 1
                    
                    sums.add(total)
                    size += 1
        
        return sorted(sums, reverse=True)[:3]