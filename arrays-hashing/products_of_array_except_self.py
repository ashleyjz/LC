# 238 medium

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)
        for i in range(len(prods)-1):
            prods[i+1] = prods[i] * nums[i]
        last_prod = 1
        for i in range(len(nums)-1, -1, -1):
            prods[i] *= last_prod
            last_prod *= nums[i]
        return prods

