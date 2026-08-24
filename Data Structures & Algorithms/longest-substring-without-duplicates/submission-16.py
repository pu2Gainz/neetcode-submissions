class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a map to record the char and last appeared index:

        l = 0 # current length = r - l + 1
        imap = {}
        res = 0
        for r in range(len(s)):
            if s[r] in imap and l <= imap[s[r]]:
                l = imap[s[r]] + 1
                imap[s[r]] = r
            else:
                imap[s[r]] = r
                res = max(res, r - l + 1)

        return res

        # tmmzuxt
        # r = 0 imap = {t: 0} l = 0
        # r = 1 imap = {t: 0, m : 1}
        # r = 2 imap = {t: 0}