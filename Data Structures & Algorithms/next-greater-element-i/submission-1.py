class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIdx = {}

        for i, num in enumerate(nums1):
            numsIdx[num] = i
        stack = []
        res = [-1] * len(nums1)
        for j in range(len(nums2)):
            while stack and stack[-1] < nums2[j]:
                n = stack.pop()
                res[numsIdx[n]] = nums2[j]
            if nums2[j] in numsIdx:
                stack.append(nums2[j])

        return res