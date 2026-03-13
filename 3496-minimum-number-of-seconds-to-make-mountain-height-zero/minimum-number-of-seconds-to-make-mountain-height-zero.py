class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        import math
        
        def can_finish(T):
            total = 0
            
            for w in workerTimes:
                val = (2*T) // w
                
                x = int((math.sqrt(1 + 4*val) - 1) // 2)
                
                total += x
                if total >= mountainHeight:
                    return True
            
            return False
        
        left, right = 1, 10**18
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans