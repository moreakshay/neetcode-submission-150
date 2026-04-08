class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        start, end = 0, len(matrix[0]) - 1
        n = 0
        while top <= bot:
            n = (bot + top) // 2
            if target < matrix[n][0]:
                bot = n - 1
            elif target > matrix[n][-1]:
                top = n + 1
            else:
                break
        
        while start <= end:
            m = (end + start) // 2
            if target < matrix[n][m]:
                end = m - 1
            elif target > matrix[n][m]:
                start = m + 1
            else: 
                return True
        return False

