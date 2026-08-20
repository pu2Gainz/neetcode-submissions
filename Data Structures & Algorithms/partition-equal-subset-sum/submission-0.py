class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # capacity len(nums) - 1
        # weight 1, cost num[i]

        M = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        N = total // 2
        pre = [0] * (N + 1)
        cur = [0] * (N + 1)

        for r in range(M):
            for c in range(1, N + 1):
                skip = pre[c]
                include = 0
                if c >= nums[r]:
                    include = nums[r] + pre[c - nums[r]]
                cur[c] = max(skip, include)
                if cur[c] == total // 2:
                    return True
            pre = cur[:]
                
        return False