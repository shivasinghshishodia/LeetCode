class Solution(object):
    def findRotation(self, mat, target):
        def rotate(matrix):
            # rotate 90° clockwise
            return [list(row) for row in zip(*matrix[::-1])]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        