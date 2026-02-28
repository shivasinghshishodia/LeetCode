class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        result = 0
        
        for i in range(1, n + 1):
            length = i.bit_length()
            result = ((result << length) | i) % MOD
        
        return result

        """
        :type n: int
        :rtype: int
        """
        