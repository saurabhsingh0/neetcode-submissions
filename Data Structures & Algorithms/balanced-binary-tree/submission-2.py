# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0 #height of a null node is 0
                
            left = height(node.left)
            right = height(node.right)

            if left is -1 or right is -1:
                return -1 #-1 indicates chidlren are imbalanced
            
            if abs(left-right) > 1:
                return -1 #current node is imbalanced
            
            return 1 + max(left, right)
        
        return height(root) != -1