class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        num = 0
        s = s.replace(" ", "")
        # 3+2*2 
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    if stack:
                        prev = stack.pop()
                        num *= prev
                        stack.append(num)
                else:
                    if stack:
                        prev = stack.pop()
                        num = int(prev / num)
                        stack.append(num)
                num = 0
                op = c
           
        return sum(stack)