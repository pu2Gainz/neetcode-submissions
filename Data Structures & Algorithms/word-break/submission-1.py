class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}
        def backtrack(i):

            if i == len(s):
                return True

            if i in cache:
                return cache[i]
            cache[i] = False
            for j in range(i , len(s)):
                w = s[i : j+1]
                if w not in wordDict:
                    continue
                if backtrack(j + 1):
                    cache[i] = True


            return cache[i]

        return backtrack(0)

        