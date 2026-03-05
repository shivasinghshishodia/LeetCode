class Solution(object):
    def minOperations(self, s):
        mismatch1 = 0  
        mismatch2 = 0  
        
        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                mismatch1 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                mismatch2 += 1
        
        return min(mismatch1, mismatch2)
        """
        :type s: str
        :rtype: int
        """
        