class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]: # right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else: # left is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1

        return -1