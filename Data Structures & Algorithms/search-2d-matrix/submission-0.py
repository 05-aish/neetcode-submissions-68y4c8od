class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix[0])
        
        while(l < len(matrix)):
            if target not in matrix[l]:
                l += 1
            else:
                return True
        return False

            
            