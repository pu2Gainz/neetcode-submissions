class LRUCache {
    Node head;
    Node tail;
    int capacity;
    Map<Integer, Node> nodeMap;

    public LRUCache(int capacity) {
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.capacity = capacity;
        this.nodeMap = new HashMap<>();
    }
    
    public int get(int key) {
        if (!this.nodeMap.containsKey(key)) {
            return -1;
        }

        Node node = nodeMap.get(key);
        Node prev = node.prev;
        Node next = node.next;

        prev.next = next;
        next.prev = prev;

        Node temp = this.head.next;
        this.head.next = node;
        node.prev = this.head;
        node.next = temp;
        temp.prev = node;
        return node.value;
    }
    
    public void put(int key, int value) {
        Node newNode = new Node(key, value);
        if (this.nodeMap.containsKey(key)) {
            // delete old node
            Node node = this.nodeMap.get(key);
            Node prev = node.prev;
            Node next = node.next;
            prev.next = next;
            next.prev = prev;
        } 

        // add new Node
        Node temp = this.head.next;
        this.head.next = newNode;
        newNode.next = temp;
        newNode.prev = head;
        temp.prev = newNode;
        this.nodeMap.put(key, newNode);

        // check capacity
        if (this.nodeMap.size() > capacity) {
            Node lru = this.tail.prev;
            Node lruPrev = lru.prev;

            lruPrev.next = this.tail;
            this.tail.prev = lruPrev;

            this.nodeMap.remove(lru.key);
        }
    }
}

class Node {
    int key;
    int value;
    Node next;
    Node prev; 
    
    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}
