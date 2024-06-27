# 15 medium

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []

        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            left = idx + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]
                if curr_sum == 0:
                    sums.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return sums
