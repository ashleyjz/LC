# 739 medium

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        highs = []
        for idx, temp in enumerate(temperatures):
            while len(highs) > 0 and temp > temperatures[highs[-1]]:
                high_idx = highs.pop()
                result[high_idx] = idx - high_idx
            highs.append(idx)
        return result

