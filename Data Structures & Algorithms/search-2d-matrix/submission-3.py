class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1
        while rl <= rr:
            rm = (rl + rr) // 2
            if matrix[rm][-1] < target: 
                rl = rm + 1
            elif matrix[rm][0] > target:
                rr = rm - 1
            else:
                break

        if not (rl <= rr):
            return False

        rl = (rl + rr) // 2

        cl, cr = 0, len(matrix[0]) - 1 

        while cl <= cr:
            cm = cl + (cr - cl) // 2
            if matrix[rl][cm] < target: 
                cl = cm + 1

            elif matrix[rl][cm] > target:
                cr = cm - 1

            else:
                return True

        return False