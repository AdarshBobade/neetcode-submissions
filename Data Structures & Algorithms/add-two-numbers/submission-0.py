# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        prev = dummy_head

        cur1 = l1
        cur2 = l2
        carry = 0

        while cur1 or cur2 or carry:

            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            new_sum = val1 + val2 + carry
            carry = new_sum // 10

            prev.next = ListNode(new_sum % 10)
            prev = prev.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy_head.next













