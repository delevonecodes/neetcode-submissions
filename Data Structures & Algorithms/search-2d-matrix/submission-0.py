class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1

        while l <= r:
            middle_array = l + ((r-l)// 2)
            if matrix[middle_array][0] <= target <= matrix[middle_array][-1]:
                return target in matrix[middle_array]
            elif target < matrix[middle_array][0]:
                r = middle_array - 1
            elif target > matrix[middle_array][-1]:
                l = middle_array + 1
        return False
