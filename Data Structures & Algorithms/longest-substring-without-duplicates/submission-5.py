class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxLength = 0
        lengthIndex = {}
        while r < len(s):
            if s[r] in lengthIndex:
                l = max(l, lengthIndex[s[r]] + 1)
                
            lengthIndex[s[r]] = r
            r += 1
            maxLength = max(maxLength, r - l)

        return maxLength