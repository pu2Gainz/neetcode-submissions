class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for string in strs: 
            if str(sorted(string)) in m: 
                m[str(sorted(string))].append(string)
            else:
                m[str(sorted(string))] = [string]
        
        return list(m.values())
