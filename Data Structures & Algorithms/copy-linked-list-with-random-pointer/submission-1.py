"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        oldToCopy = {}
        curr = head

        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        second = head
        oldToCopy[None] = None
        while second:
            oldToCopy[second].next = oldToCopy[second.next]
            oldToCopy[second].random = oldToCopy[second.random]
            second = second.next

        return oldToCopy[head]


       
            
        




        