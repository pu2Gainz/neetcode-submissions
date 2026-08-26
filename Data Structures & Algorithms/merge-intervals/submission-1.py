class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = []
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                prev = stack.pop()
                interval = [prev[0], max(prev[1],interval[1])]
            
            stack.append(interval)
        
        return stack
