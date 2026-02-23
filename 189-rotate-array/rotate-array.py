class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        