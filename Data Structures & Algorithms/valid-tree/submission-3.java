class Solution {
    HashMap<Integer, ArrayList<Integer>> adj;
    HashSet<Integer> visited;
    HashSet<Integer> visiting;

    public boolean validTree(int n, int[][] edges) {
        adj = new HashMap<>();
        visited = new HashSet<>();
        visiting = new HashSet<>();

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            adj.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
        }

        if (!dfs(0, -1)) return false;
        return visited.size() == n;
    }

    private boolean dfs(int n, int parent) {
        if (visited.contains(n)) return true;
        if (visiting.contains(n)) return false;

        visiting.add(n);
        for (int child : adj.getOrDefault(n, new ArrayList<>())) {
            if (child == parent) continue;
            if (!dfs(child, n)) return false;
        }
        visiting.remove(n);
        visited.add(n);
        return true;
    }
}
