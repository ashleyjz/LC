# 128 medium

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        count = 0
        for num in unique_nums:
            if num-1 not in unique_nums:
                curr_len = 1
                while num + curr_len in unique_nums:
                    curr_len += 1
                count = max(count, curr_len)
        return count
