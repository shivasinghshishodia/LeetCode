class Solution(object):
    def hasAllCodes(self, s, k):
        if len(s) < k + (2**k) - 1:
            return False
        
        seen = set()
    
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == 2**k:
                return True
            
        return False
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        