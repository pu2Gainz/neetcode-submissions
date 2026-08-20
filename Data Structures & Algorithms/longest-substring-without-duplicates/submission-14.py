class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        imap = {}

        for r in range(len(s)):
            if s[r] in imap and imap[s[r]] >= l:
                l = imap[s[r]] + 1
            
            length = max(length, r - l + 1)
            imap[s[r]] = r

        return length