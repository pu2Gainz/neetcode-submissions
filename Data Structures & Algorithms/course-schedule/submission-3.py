class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visiting = set()
        visited  = set()

        def dfs(course):
            if course in visited:
                return True

            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)

            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        
        return True