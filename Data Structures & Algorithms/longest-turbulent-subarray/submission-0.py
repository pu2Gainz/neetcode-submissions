class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        flip = 0 # 1 means >  and -1 means <

        l = 0
        length = 1
        
        for r in range(1, len(arr)):
            if flip == 0:
                if arr[r] - arr[r - 1] > 0:
                    flip = -1
                elif arr[r] - arr[r - 1] < 0:
                    flip = 1
                else:
                    l = r
            elif flip == 1:
                if arr[r] - arr[r - 1] > 0:
                    flip = -1
                elif arr[r] - arr[r - 1] < 0:
                    l = r - 1
                else:
                    flip = 0
                    l = r
            elif flip == -1:
                if arr[r] - arr[r - 1] > 0:
                    l = r - 1
                elif arr[r] - arr[r - 1] < 0:
                    flip = 1
                else:
                    flip = 0
                    l = r
            length = max(length, r - l + 1)

        return length
