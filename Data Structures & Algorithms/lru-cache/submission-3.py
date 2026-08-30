class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])

        node = Node(key, value)
        self.insert(node)
        self.nodeMap[key] = node


        if len(self.nodeMap) > self.capacity:
            n = self.left.next
            self.remove(n)
            del self.nodeMap[n.key]
   
