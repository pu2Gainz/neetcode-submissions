"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodeMap = {}
        queue = deque([node])
        nodeMap[node] = Node(node.val)

        while queue:
            original = queue.popleft()
            for n in original.neighbors:
                if n not in nodeMap:
                    nodeMap[n] =  Node(n.val)
                    queue.append(n)
                nodeMap[original].neighbors.append(nodeMap[n])
        
        return nodeMap[node]

            
        