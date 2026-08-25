class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            print(m)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        return nums[l]

    #  l 0 -> 3
    #  r 5 -> 4
    #  m 2 -> 4
    #  nums[l] 6
    #  nums[r] 1
    #  nums[m] 1