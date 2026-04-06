class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        last_row = matrix[len(matrix)-1]
        if target > last_row[len(last_row)-1]:
            return False

        left = 0
        right = len(matrix)-1
        while left<=right:
            mid = left + (right - left) // 2
            cell_left = 0
            cell_right = len(matrix[mid])-1
            if target < matrix[mid][cell_left]:
                right = mid -1
            elif target > matrix[mid][cell_right]:
                left = mid + 1
            else:
                while cell_left <= cell_right:
                    cell_middle = cell_left + (cell_right - cell_left) // 2
                    if matrix[mid][cell_middle] > target:
                        cell_right = cell_middle - 1
                    elif matrix[mid][cell_middle] < target:
                        cell_left = cell_middle + 1
                    else:
                        return True
                return False
        return False