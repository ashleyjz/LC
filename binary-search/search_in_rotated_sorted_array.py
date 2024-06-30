# 33 medium

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            curr = (left + right) // 2
            if nums[curr] == target:
                return curr
            if nums[curr] > nums[right]:
                if nums[curr] < target:
                    right = curr - 1
                else:
                    left = curr + 1
            else:
                if nums[curr] < target:
                    left = curr + 1
                else:
                    right = curr - 1
        return -1