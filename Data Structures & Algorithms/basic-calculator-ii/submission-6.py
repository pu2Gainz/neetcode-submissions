class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        s = s.replace(" ", "")
        num = 0

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if not c.isdigit() or i == len(s) - 1:
                if op =="+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    if stack:
                        prev = stack.pop()
                        stack.append(prev * num)

                else: 
                    if stack:
                        prev = stack.pop()
                        stack.append(int(prev / num))

                op = c
                num = 0

        return sum(stack)