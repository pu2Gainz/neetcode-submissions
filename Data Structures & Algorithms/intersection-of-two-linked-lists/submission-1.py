# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()

        while headA or headB:
            if headA:
                if headA in node_set:
                    return headA
                node_set.add(headA)
                headA = headA.next
            if headB:
                if headB in node_set:
                    return headB
                node_set.add(headB)
                headB = headB.next


        return None