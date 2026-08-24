class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # r - l + 1 - oneCounter = current number of 0s

        l = 0
        oneCounter = 0
        res = 0 
        for r in range(len(nums)):
            if nums[r] == 1 or r - l + 1 - oneCounter <= k:
                oneCounter += nums[r]
                res = max(res, r - l + 1)
            else:
                while r - l + 1 - oneCounter > k:
                    oneCounter -= nums[l]
                    l += 1

        return res