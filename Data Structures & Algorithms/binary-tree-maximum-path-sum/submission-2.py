# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def helper(root):
            if not root:
                return 0 

            left_val = max(0, helper(root.left))
            right_val = max(0, helper(root.right))

            current_sum = root.val + left_val + right_val
            if self.max_sum < current_sum:
                self.max_sum = current_sum
            
            return root.val + max(left_val, right_val)

        helper(root)

        return self.max_sum
            

        
        
        


            
        