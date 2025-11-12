from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d_queue = deque([root])
        depth = 0
        while d_queue:
            depth += 1
            for _ in range(len(d_queue)):
                t = d_queue.popleft()
                if t.left:
                    d_queue.append(t.left)
                if t.right:
                    d_queue.append(t.right)
        return depth