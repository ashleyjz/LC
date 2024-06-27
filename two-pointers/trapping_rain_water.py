# 42 hard

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        area = 0
        max_left = 0
        max_right = 0
        for idx in range(len(height)):
            if idx > 0:
                max_left = max(max_left, height[idx-1])
            max_right = height[len(height)-1]
            for i in range(len(height)-2, idx, -1):
                max_right = max(max_right, height[i])
            temp = min(max_left, max_right) - height[idx]
            # print(f'left:{max_left}, right:{max_right}, area:{temp}')
            if temp >= 0:
                area += temp
        return area

