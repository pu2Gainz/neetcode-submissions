class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            preMap[course].append(pre)

        path  = []
        visiting = set()

        def dfs(n):
            if n in visiting:
                return False
            if preMap[n] == []:
                if n not in path:
                    path.append(n)
                return True
            
            visiting.add(n)

            for pre in preMap[n]:
                if not dfs(pre):
                    return False
            
            visiting.remove(n)
            preMap[n] = []
            path.append(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return path