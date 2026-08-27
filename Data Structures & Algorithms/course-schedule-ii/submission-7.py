class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visiting = set()
        path = []

        def dfs(course):
            if course in visiting:
                print("Course in visiting: " + str(course))
                return False
            if course in path:
                return True

            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            path.append(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return path


