class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for string in strs: 
            l = [0] * 26
            for char in string: 
                l[ord(char) - ord('a')] += 1
            m[tuple(l)].append(string)
            
        return list(m.values())
