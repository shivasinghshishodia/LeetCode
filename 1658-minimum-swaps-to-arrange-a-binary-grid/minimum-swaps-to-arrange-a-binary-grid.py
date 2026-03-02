class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: Greedy row fixing
        for i in range(n):
            required = n - i - 1
            j = i
            
            # Find row that satisfies requirement
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # Bring row up by swapping
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        