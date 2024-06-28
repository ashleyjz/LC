# 22 medium

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def iterate(curr: str, left: int, right: int):
            if len(curr) == n * 2:
                ans.append(curr)
                return
            if left < n:
                iterate(curr + '(', left+1, right)
            if right < left:
                iterate(curr + ')', left, right+1)
        iterate('', 0, 0)
        return ans
