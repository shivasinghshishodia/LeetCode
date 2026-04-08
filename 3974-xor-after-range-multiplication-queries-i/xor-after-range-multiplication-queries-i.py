class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        
        # compute XOR
        result = 0
        for num in nums:
            result ^= num
        
        return result
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        