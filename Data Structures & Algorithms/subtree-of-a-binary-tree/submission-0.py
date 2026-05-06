# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it can't contain any subRoot
        if not root:
            return False
        
        # 1. Check if the current tree matches subRoot exactly
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. If not, search in the left and right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both must reach NULL at the same time to be identical
        if not p and not q:
            return True
        
        # If only one is NULL, or values don't match, they aren't the same
        if not p or not q or p.val != q.val:
            return False
        
        # Check structure and values of children recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)