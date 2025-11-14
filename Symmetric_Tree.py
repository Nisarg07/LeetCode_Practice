# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left,root.right)


    def is_mirror(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        outer_mirror = self.is_mirror(p.left,q.right)
        inner_mirror = self.is_mirror(p.right,q.left)

        return outer_mirror and inner_mirror
        