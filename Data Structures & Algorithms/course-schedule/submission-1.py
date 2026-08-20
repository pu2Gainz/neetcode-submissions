class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(n):
            if n in visiting:
                return False
            if preMap[n] == []:
                return True

            visiting.add(n)
            for pre in preMap[n]:
                if dfs(pre): 
                    preMap[n].remove(pre)
                else:
                    return False
            visiting.remove(n)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True