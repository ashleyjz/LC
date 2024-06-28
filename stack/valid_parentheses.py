# 20 easy

class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                parens.append(ch)
                continue
            if len(parens) == 0:
                return False
            elif ((ch == ')' and parens[-1] != '(')
                or (ch == ']' and parens[-1] != '[')
                or (ch == '}' and parens[-1] != '{')):
                return False
            else:
                parens.pop()
        return len(parens) == 0