class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        isNewIntervalInserted = False
        for i, interval in enumerate(intervals):
            #if overlaps, merge interval and new interval
            if interval[0] <=  newInterval[1] and interval[1] >= newInterval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            #if before new interval, append:
            elif interval[1] <= newInterval[0]:
                stack.append(interval)
            #if after new interval, append newInterval and rest of the intervals
            else: 
                stack.append(newInterval)
                isNewIntervalInserted = True
                stack += (intervals[i:])
                break
        if not isNewIntervalInserted:
            stack.append(newInterval)
        return stack