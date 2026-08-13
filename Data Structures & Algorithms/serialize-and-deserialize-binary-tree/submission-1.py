# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return 'null'
            
        queue = deque([root])
        result = []

        while queue:

            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        values = data.split(",")
        if values[0] == 'null':
            return None
    
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            
            current = queue.popleft()

            if values[i] != 'null':
                current.left = TreeNode(int(values[i]))
                queue.append(current.left)

            if values[i + 1] != 'null':
                current.right = TreeNode(int(values[i + 1]))
                queue.append(current.right)

            i += 2
        
        return root

            
        


        





