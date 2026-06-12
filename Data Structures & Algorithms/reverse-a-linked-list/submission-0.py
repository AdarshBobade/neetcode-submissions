# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        else:
            
            prev = None
            cur = head
            while cur is not None:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            # head = cur.next

        return prev
                



        