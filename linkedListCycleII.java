/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        List<ListNode> posList = new ArrayList<>();
        ListNode curr = head;
        while (curr != null) {
            if (posList.contains(curr)) {
                return curr;
            } else {
                posList.add(curr);
            }
            curr = curr.next;
        }
        return null;    
    }
}
