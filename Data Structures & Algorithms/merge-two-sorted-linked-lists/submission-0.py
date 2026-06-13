# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        cur1 = list1
        cur2 = list2
        prev = dummy_node
        
        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val :
                prev.next = cur1
                prev = cur1
                cur1 = cur1.next
                
            else :
                prev.next = cur2
                prev = cur2
                cur2 = cur2.next
                

        if cur2 is None:
            while cur1 is not None:
                prev.next = cur1
                prev = cur1
                cur1 = cur1.next

        elif cur1 is None:
            while cur2 is not None:
                prev.next = cur2
                prev = cur2
                cur2 = cur2.next
        return dummy_node.next











        