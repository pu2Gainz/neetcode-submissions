class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest = 0
        for num in nums:
            s.add(num)

        for num in nums:
            if num - 1 in s:
                continue
            curLength = 1

            while num + 1 in s:
                num += 1
                curLength += 1

            longest = max(longest, curLength)

        return longest