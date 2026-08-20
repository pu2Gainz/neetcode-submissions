class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # valueIndex = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in valueIndex:
        #         return [valueIndex[target - numbers[i]] + 1, i + 1]
        #     valueIndex[numbers[i]] = i

        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l + 1, r + 1]
            elif curSum < target:
                l += 1
            else:
                r -= 1
        
