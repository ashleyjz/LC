# 3 medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substr = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[right])
            length = max(length, right - left + 1)
        return length