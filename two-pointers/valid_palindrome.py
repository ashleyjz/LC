# 125 easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alnum(ch: str):
            return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))

        left = 0
        right = len(s) - 1
        while left < right:
            if not is_alnum(s[left]):
                left += 1
                continue
            if not is_alnum(s[right]):
                right -= 1
                continue
            if is_alnum(s[left]) and is_alnum(s[right]):
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
