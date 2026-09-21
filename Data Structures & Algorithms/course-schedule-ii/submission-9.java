class Solution {
    HashMap<Integer, ArrayList<Integer>> preMap;
    HashSet<Integer> visited;
    HashSet<Integer> visiting;
    ArrayList<Integer> path;
    int[][] directions;
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        preMap = new HashMap<>();
        for (int[] prereq : prerequisites) {
            int course = prereq[0];
            int pre = prereq[1];
            preMap.computeIfAbsent(course, k -> new ArrayList<>()).add(pre);
        }

        visited = new HashSet<>();
        visiting = new HashSet<>();
        path = new ArrayList<>();

        for (int n = 0; n < numCourses; n++) {
            if (!dfs(n)) return new int[]{};
        }

        int[] res = new int[path.size()];

        for (int i = 0; i < path.size(); i++) {
            res[i] = path.get(i);
        }

        return res;
    }

    public boolean dfs(int course) {
        if (visited.contains(course)) return true;
        if (visiting.contains(course)) return false;

        visiting.add(course);

        for (int pre : preMap.getOrDefault(course, new ArrayList<>())) {
            if (!dfs(pre)) return false;
        }
        visiting.remove(course);
        visited.add(course);
        path.add(course);
        return true;

    }
}
