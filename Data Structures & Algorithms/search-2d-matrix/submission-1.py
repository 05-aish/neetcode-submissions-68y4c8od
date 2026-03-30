class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix[0])
        n = len(matrix)
        h = (m * n) - 1

        while(l <= h):
            mid = l + (h - l) // 2
            row = mid // (m)
            col = mid % (m)

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                h = mid - 1
        return False

            
            