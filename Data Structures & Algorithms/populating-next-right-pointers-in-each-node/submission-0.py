"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q1 = deque([root])
        while q1 :
            
            qLen = len(q1)
            
            for i in range(qLen) :
                node = q1.popleft()
    
                if i + 1 == qLen : 
                    node.next = None
                else : 
                    node.next = q1[0]
                if node.left :
                    q1.append(node.left)
                if node.right :
                    q1.append(node.right)
        return root
                











        