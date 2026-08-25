class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store [t, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < t:
                    t1, i1 = stack.pop()
                    res[i1] = i - i1
            stack.append([t, i])
        
        return res