class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        s = s.replace(" ", "")
        num = 0
        print(s)
        for c in s + "+":
            if not c.isdigit():
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                op = c
            else: 
                num = num * 10 + int(c)
        return sum(stack)
        #3+2*2
        # c: 3 -> + -> 2 -> * -> 2 
        # num: 3 -> 0 -> 2 -> 0 -> 2
        # op: + -> + -> * 
        # stack: [3, 2, ] 
