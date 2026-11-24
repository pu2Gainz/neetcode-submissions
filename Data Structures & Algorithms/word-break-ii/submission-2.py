class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}
        def backtrack(i):

            if i == len(s):
                return [""]
            res = []

            if i in cache:
                return cache[i]

            for j in range(i, len(s)):
                w = s[i: j+1]
                if w not in wordDict:
                    continue
                strings = backtrack(j + 1)

                for string in strings:
                    sentence = w
                    if string:
                        sentence += " " + string
                    res.append(sentence)
            cache[i] = res
            return res    
    
        return backtrack(0)
