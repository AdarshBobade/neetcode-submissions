# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head , head.next
        last_node,cur = head,head
        dummy_node = ListNode(0)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        # dummy_node.next = cur.next
        # cur = dummy_node.next
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        l1 = head
        l2 = prev
        while l2:
            first = l1.next
            second = l2.next
            l1.next = l2
            l2.next = first
            l1 = first
            l2 = second

        


        



        