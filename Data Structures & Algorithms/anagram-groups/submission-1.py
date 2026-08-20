class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for string in strs: 
            l = [0] * 26
            for char in string: 
                l[ord(char) - ord('a')] += 1
            if tuple(l) in m:
                m[tuple(l)].append(string)
            else:
                m[tuple(l)] = [string]
        return list(m.values())
