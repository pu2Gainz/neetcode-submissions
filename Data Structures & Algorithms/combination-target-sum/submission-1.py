class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(i, comb, total):

            if total == target:
                res.append(comb.copy())
                return

            for j in range(i, n):
                if total + nums[j] > target:
                    return
                comb.append(nums[j])
                backtrack(j, comb, total + nums[j])
                comb.pop()
            
        backtrack(0, [], 0)
        return res