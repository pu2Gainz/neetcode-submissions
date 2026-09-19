/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        HashMap<Node, Node> oldToNew = new HashMap<>();
        Node copy = new Node(node.val);
        Queue<Node> queue = new ArrayDeque<>();

        queue.offer(node);
        oldToNew.put(node, copy);

        while (!queue.isEmpty()) {
            Node n = queue.poll();
            
            for (Node nei : n.neighbors) {
                Node nCopy = oldToNew.get(n);
                if (!oldToNew.containsKey(nei)) {
                    Node neiCopy = new Node(nei.val);
                    oldToNew.put(nei, neiCopy);
                    queue.add(nei);
                }
                nCopy.neighbors.add(oldToNew.get(nei));
            }
        }

        return oldToNew.get(node);
    }

}