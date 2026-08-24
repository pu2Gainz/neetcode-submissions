class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        index = [0] * len(fruits)
        curTypes = []
        res = 0
        l = 0
        for r in range(len(fruits)):
            if len(curTypes) == 2 and fruits[r] not in curTypes:
                index1, index2 = index[curTypes[0]], index[curTypes[1]]
                if index1 < index2: 
                    curTypes.remove(curTypes[0])
                    l = index1 + 1
                else:
                    curTypes.remove(curTypes[1])
                    l = index2 + 1
                curTypes.append(fruits[r])
            else: 
                if fruits[r] not in curTypes:
                    curTypes.append(fruits[r])
            res = max(res, r - l + 1)
            index[fruits[r]] = r

        return res





