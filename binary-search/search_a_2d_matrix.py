# 74 medium

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        row = -1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        # print(f'row:{row}')

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            half = (left + right) // 2
            if matrix[row][half] < target:
                left = half + 1
            elif matrix[row][half] > target:
                right = half - 1
            else:
                return True
        return False