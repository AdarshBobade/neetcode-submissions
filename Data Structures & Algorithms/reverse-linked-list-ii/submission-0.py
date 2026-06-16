# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        prev = None
        cur = head
        while cur and cur.next and count != left:
            prev = cur
            cur = cur.next
            count += 1
        left_node = cur   # Node at position left
        tmp = prev      #Node before left

        prev = None
        while count <= right and cur :
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1

        left_node.next = cur
        if tmp:
            tmp.next = prev
        else:
            head = prev
        
        return head