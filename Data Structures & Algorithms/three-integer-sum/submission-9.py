class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1

        return res
    # -4, -1, -1, 0, 1, 2 
    # l = -1 r = 2