"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next
        oldToNew[None] = None
        cur2 = head
        while cur2:
            newNode = oldToNew[cur2]
            newNode.next = oldToNew[cur2.next]
            newNode.random = oldToNew[cur2.random]
            cur2 = cur2.next
        
        return oldToNew[head]
        