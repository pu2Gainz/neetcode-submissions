class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        res = 1
        prev = nums[0]
        length = 1
        for num in nums:
            if num == prev:
                continue
            elif num > prev + 1:
                length = 1
                prev = num
            else:
                length += 1
                prev = num
                res = max(length, res)

        return res