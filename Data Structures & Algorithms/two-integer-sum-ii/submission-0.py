class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        valueIndex = {}
        for i in range(len(numbers)):
            if target - numbers[i] in valueIndex:
                return [valueIndex[target - numbers[i]] + 1, i + 1]
            valueIndex[numbers[i]] = i

        