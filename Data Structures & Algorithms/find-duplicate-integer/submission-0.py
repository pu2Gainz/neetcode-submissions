class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        for i in nums:
            if i in mySet:
                return i
            mySet.add(i)

        