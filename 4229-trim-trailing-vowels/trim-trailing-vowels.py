class Solution(object):
    def trimTrailingVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        last_valid_index = -1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in vowels:
                last_valid_index = i
                break
        
        if last_valid_index == -1:
            return ""
        
        return s[:last_valid_index + 1]
        """
        :type s: str
        :rtype: str
        """
        