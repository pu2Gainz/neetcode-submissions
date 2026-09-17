/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;

        int carry = 0;

        while (l1 != null || l2 != null) {
            int v1;
            int v2;
            if (l1 == null) {
                v1 = 0;
                v2 = l2.val;
                l2 = l2.next;

            } else if (l2 == null) {
                v1 = l1.val;
                v2 = 0;
                l1 = l1.next;
            } else {
                v1 = l1.val;
                v2 = l2.val;
                l1 = l1.next;
                l2 = l2.next;
            }

            int v = (v1 + v2 + carry) % 10;
            carry = (v1 + v2 + carry) / 10;

            cur.next = new ListNode(v);
            cur = cur.next;
            
        }

        if (carry != 0) {
            cur.next = new ListNode(carry);
        }
        return dummy.next;

    }
}
