/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        Stack<ListNode> stack = new Stack<ListNode>();

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (head != null) {
            stack.Push(new ListNode(head.val));
            head = head.next;
        }

        while (stack.Count > 0){
            curr.next = stack.Pop();
            curr = curr.next;
        }

        return dummy.next;
    }
}