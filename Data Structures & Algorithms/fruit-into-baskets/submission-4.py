class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = []
        indexMap = {}
        l = 0
        res = 0
        for r in range(len(fruits)):
            if len(types) < 2:
                if fruits[r] not in types:
                    types.append(fruits[r])
                indexMap[fruits[r]] = r
            else:
                if fruits[r] not in types:
                    index1 = indexMap[types[0]]
                    index2 = indexMap[types[1]]

                    if index1 < index2:
                        types.pop(0)
                        l = index1 + 1
                    else: 
                        types.pop(1)
                        l = index2 + 1
                    types.append(fruits[r])
                indexMap[fruits[r]] = r
            res = max(res, r - l + 1)

        return res
                

