class Solution(object):
    def minimumDistance(self, nums):
        pos = {}
        
        # store indices for each value
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        
        ans = float('inf')
        
        # check each group
        for key in pos:
            indices = pos[key]
            
            if len(indices) < 3:
                continue
            
            # check consecutive triplets
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i+2] - indices[i])
                if dist < ans:
                    ans = dist
        
        return ans if ans != float('inf') else -1
        
        """
        :type nums: List[int]
        :rtype: int
        """
        