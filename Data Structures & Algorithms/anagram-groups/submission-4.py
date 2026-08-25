class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = defaultdict(list)
        for s in strs:
            sMap["".join(sorted(s))].append(s)
        
        res = []
        for item in sMap.values():
            res.append(item)
        return res