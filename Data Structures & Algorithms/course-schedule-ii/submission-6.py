class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        path = []
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            path.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return path