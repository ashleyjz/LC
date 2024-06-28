# 84 hard

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bars = []
        max_area = 0
        for idx in range(len(heights)):
            if idx == 0:
                bars.append((idx, heights[idx]))
                continue
            next_idx = idx
            while len(bars) > 0 and heights[idx] < bars[-1][1]:
                next_idx, bar = bars.pop()
                max_area = max(max_area, bar * (idx - next_idx))
            bars.append((next_idx, heights[idx]))

        for (idx, height) in bars:
            max_area = max(max_area, height * (len(heights)-idx))
        return max_area
