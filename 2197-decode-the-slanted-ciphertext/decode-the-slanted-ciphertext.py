class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # rebuild matrix
        mat = []
        idx = 0
        for i in range(rows):
            mat.append(list(encodedText[idx:idx+cols]))
            idx += cols
        
        # read diagonally
        res = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            
            while i < rows and j < cols:
                res.append(mat[i][j])
                i += 1
                j += 1
        
        return "".join(res).rstrip()
        