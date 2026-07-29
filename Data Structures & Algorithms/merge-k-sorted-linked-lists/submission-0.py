# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(cur1 ,cur2):
            dummy_head = ListNode(0)
            cur = dummy_head
            while cur1 and cur2 :
                if cur1.val <= cur2.val :
                    cur.next = cur1
                    cur = cur1
                    cur1 = cur1.next
                elif cur1.val > cur2.val :
                    cur.next = cur2
                    cur = cur2
                    cur2 = cur2.next

            if not cur1:
                while cur2 :
                    cur.next = cur2
                    cur = cur2
                    cur2 = cur2.next
            elif not cur2 :
                while cur1 :
                    cur.next = cur1
                    cur = cur1
                    cur1 = cur1.next

            return dummy_head.next
        
        if lists:
            prev = lists[0]
        else :
            return None
        for i in range(1 , len(lists)):
            prev = mergeTwoLists(prev , lists[i])
        return prev











