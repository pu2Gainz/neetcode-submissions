class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def backtrack(i):

            if i == len(s):
                return [""]
            res = []

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
            return res    
    
        return backtrack(0)
