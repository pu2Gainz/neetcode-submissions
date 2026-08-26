class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            #if interval overlapps with newInterval, then merge them
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                res.append(interval)

        res.append(newInterval)
        return res
