class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()
        visiting = set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if pre in visited:
                    continue
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
