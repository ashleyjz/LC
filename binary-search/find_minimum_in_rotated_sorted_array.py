# 153 medium

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_num = nums[0]
        while left <= right:
            curr = (left + right) // 2
            min_num = min(min_num, nums[curr])
            if nums[curr] > nums[right]:
                left = curr + 1
            else:
                right = curr - 1
        return min_num