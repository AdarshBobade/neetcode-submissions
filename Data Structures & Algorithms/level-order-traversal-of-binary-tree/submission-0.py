# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([])
        if not root :
            return res
        queue.append(root)
        while queue :
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                new = queue.popleft()
                level.append(new.val)
                if new.left :
                    queue.append(new.left)
                if new.right :
                    queue.append(new.right)
                
            res.append(level)
        return res




