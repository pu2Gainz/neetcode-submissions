class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            mid = left + (right - left) // 2
            rm = mid // COLS
            cm = mid % COLS

            if matrix[rm][cm] == target:
                return True

            elif matrix[rm][cm] < target:
                left = mid + 1
            else:
                right = mid - 1
        

        return False