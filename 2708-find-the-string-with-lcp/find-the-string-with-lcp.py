class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        word = [''] * n
        curr_char = 0
        
        for i in range(n):
            if word[i] == '':
                if curr_char >= 26:
                    return ""
                
                ch = chr(ord('a') + curr_char)
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = ch
                
                curr_char += 1
        
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return "".join(word)
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        