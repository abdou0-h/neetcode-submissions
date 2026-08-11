# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # إذا كانت الشجرة فارغة
        if not root:
            return []

        # إنشائ الطابور ووضع جذر الشجرة كبداية
        queue = deque([root])
        result = []

        while queue:
           
            length = len(queue)
            current = []
            for _ in range(length):
                node = queue.popleft()
                current.append(node.val)
            
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            result.append(current)

        return result