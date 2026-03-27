class Solution(object):
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        
        shift = k % n
        
        for i in range(m):
            for j in range(n):
                
                if i % 2 == 0:  # even row → left shift
                    new_j = (j + shift) % n
                else:           # odd row → right shift
                    new_j = (j - shift) % n
                
                if mat[i][j] != mat[i][new_j]:
                    return False
        
        return True
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        