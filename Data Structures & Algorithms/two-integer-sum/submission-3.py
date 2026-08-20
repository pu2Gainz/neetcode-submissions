class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for i in range(len(nums)):
            if nums[i] in prevMap:
                return [prevMap[nums[i]], i]

            prevMap[target - nums[i]] = i
        
        