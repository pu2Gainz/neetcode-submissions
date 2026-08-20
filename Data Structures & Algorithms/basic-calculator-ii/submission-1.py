class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        s = s.replace(' ', '')

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-': 
                    stack.append(-num)
                elif op == '*':
                    num *= stack.pop()
                    stack.append(num)
                else:
                    stack.append(int(stack.pop() / num))
                op = ch
                num = 0

        return sum(stack)