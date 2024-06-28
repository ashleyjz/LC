# 150 medium

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def arithmetic(a: int, b: int, op: str) -> int:
            print(f'a:{a}, b:{b}')
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                if a == 0 or b == 0:
                    return 0
                return int(float(a) / b)

        ans = []
        for tok in tokens:
            if tok == '+' or tok == '-' or tok == '*' or tok == '/':
                b = ans.pop()
                a = ans.pop()
                ans.append(arithmetic(a, b, tok))
            else:
                ans.append(int(tok))
        return ans[0]