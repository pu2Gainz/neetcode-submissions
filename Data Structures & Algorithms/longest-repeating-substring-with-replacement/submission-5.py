class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        freq = {}
        l = 0

        maxFreq = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            while maxFreq + k < r - l + 1: 
                freq[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

        return length
