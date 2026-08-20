class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rt = 0
        rb = len(matrix) - 1
        cl = 0
        cr = len(matrix[0]) - 1

        row = 0
        # find in which row 
        while rt <= rb:
            rm = rt + (rb - rt) // 2
            if matrix[rm][cr] >= target >= matrix[rm][cl]:
                row = rm 
                break
            elif matrix[rm][cl] > target:
                rb = rm - 1 
            elif matrix[rm][cr] < target:
                rt = rm + 1
        
        # now find in the row

        while cl <= cr:
            cm = cl + (cr - cl) // 2
            
            if matrix[row][cm] == target:
                return True
            elif matrix[row][cm] > target:
                cr = cm - 1
            else:
                cl = cm + 1

        return False

