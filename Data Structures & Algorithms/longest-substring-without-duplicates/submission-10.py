class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        imap = {}

        for r in range(len(s)):
            if s[r] in imap:
                # update l pointer to the next of last occurance of s[r]
                l = max(l, imap[s[r]] + 1)
            imap[s[r]] = r
            length = max(length, r - l + 1)

        return length

            