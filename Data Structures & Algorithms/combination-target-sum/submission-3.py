class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(i, curStr, curSum):
            if curSum == target:
                res.append(curStr.copy())
                return
            for j in range(i, len(nums)):
                if curSum + nums[j] > target:
                    break
                curStr.append(nums[j])
                backtrack(j, curStr, curSum + nums[j])
                curStr.pop()

            

        backtrack(0, [], 0)
        return res