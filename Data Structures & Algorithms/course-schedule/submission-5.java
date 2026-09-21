class Solution {
        HashMap<Integer, ArrayList<Integer>> preMap;
        HashSet<Integer> visited;
        HashSet<Integer> visiting;
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        preMap = new HashMap<>();
        visited = new HashSet<>();
        visiting = new HashSet<>();
        for (int[] prereq : prerequisites) {
            int pre = prereq[1];
            int course = prereq[0];
            if (!preMap.containsKey(course)) {
                preMap.put(course, new ArrayList<>());
            }

            preMap.get(course).add(pre);
        }

        for (int n = 0; n < numCourses; n++) {
            if (!dfs(n)) return false;
        }

        return true;
        
    }

    private boolean dfs(int n) {
        if (visited.contains(n)) return true;
        if (visiting.contains(n)) return false;

        visiting.add(n);

        for (int pre : preMap.getOrDefault(n, new ArrayList<>())) {
            if (!dfs(pre)) return false;
        }
        visiting.remove(n);
        visited.add(n);
        return true;
    }
}
