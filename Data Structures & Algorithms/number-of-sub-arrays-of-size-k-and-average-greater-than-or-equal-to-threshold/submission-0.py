class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k

        currSum = 0
        l = 0
        count = 0

        for r in range(len(arr)):
            if r - l + 1 < k:
                currSum += arr[r]
            if r - l + 1 == k:
                currSum += arr[r]
                if currSum >= threshold:
                    count += 1
                currSum -= arr[l]
                l += 1
            r += 1


        return count