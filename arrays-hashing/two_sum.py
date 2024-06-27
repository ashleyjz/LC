# 1 easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for idx, num in enumerate(nums):
            needed = target - num
            if needed in indexes:
                return [indexes[needed], idx]
            indexes[num] = idx
