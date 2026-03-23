class Solution(object):
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        
        # full weeks
        total = 7 * (weeks * (weeks + 1) // 2) + 21 * weeks
        
        # remaining days
        start = weeks + 1
        for i in range(days):
            total += start + i
        
        return total
        """
        :type n: int
        :rtype: int
        """
        