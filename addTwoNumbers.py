# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        dummy = ListNode()
        head = dummy
        while (l1 or l2):
            if l1:
                val1 = l1.val
            else:
                val1 = 0
                
            if l2:
                val2 = l2.val
            else:
                val2 = 0
                
            curr_sum = val1 + val2 + carry
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            
            new_node = ListNode()
            new_node.val = curr_sum
            dummy.next = new_node
            
            # Update pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            dummy = dummy.next
            if carry != 0:
                newnode = ListNode(1)
                dummy.next = newnode
            
            
        return head.next
