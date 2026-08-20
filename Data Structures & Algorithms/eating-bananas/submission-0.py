class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r - l) // 2
            hour = 0
            for i in piles:
                hour += math.ceil(i / k)

            if hour <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res