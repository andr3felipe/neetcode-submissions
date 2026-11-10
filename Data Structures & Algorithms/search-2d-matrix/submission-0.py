class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        i = 0

        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[mid][0] and target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
            elif target < matrix[mid][0] and target < matrix[mid][len(matrix[mid]) - 1]:
                right = mid - 1
            else:
                i = mid
                break;
        
        left, right = 0, len(matrix[i]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[i][mid]:
                left = mid + 1
            elif target < matrix[i][mid]:
                right = mid - 1
            else:
                return True
        
        return False
        