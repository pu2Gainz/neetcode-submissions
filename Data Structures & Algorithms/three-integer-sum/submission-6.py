class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if num > 0: 
                return res
            else:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    three_sum = nums[l] + nums[r] + num
                    if three_sum > 0:
                        r -= 1
                    elif three_sum < 0:
                        l += 1
                    else:
                        res.append([num, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1

                    
        return res
        
                    