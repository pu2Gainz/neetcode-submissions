class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = [[] for i in range(numCourses)]

        for course, pre in prerequisites:
            preMap[course].append(pre)

        path  = []
        visiting = set()
        visited = set()

        def dfs(n):
            if n in visiting:
                return False
            if n in visited:
                return True
            
            visiting.add(n)

            for pre in preMap[n]:
                if not dfs(pre):
                    return False
            
            visiting.remove(n)
            visited.add(n)
            path.append(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return path