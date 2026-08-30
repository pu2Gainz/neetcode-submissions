# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy 
        while True:            
            kth = self.getKth(groupPrev, k)
            
            if not kth:
                break
            
            groupStart = groupPrev.next
            groupNext = kth.next

            cur = groupStart
            prev = groupNext

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            
            # groupPrev -> { 1(groupPrev.next), 2, 3(kth) } -> groupNext
            # groupPrev -> { 3, 2, 1} -> groupNext
            groupPrev.next = kth
            groupPrev = groupStart


        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next

        return curr
    
    # dummy - 1 - 2 - 3  start: 1 2 3 K: 3 2 1 