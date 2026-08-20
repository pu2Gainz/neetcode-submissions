class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)

        streak = 0

        for num in nums:
            nextNum = num + 1
            counter = 1
            while nextNum in s:
                nextNum += 1
                counter += 1
            streak = max(streak, counter)

        return streak

        