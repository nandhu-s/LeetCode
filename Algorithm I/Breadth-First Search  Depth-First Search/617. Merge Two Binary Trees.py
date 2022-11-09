# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def add(n1,n2):
            if n1 and n2:
                root=TreeNode(n1.val + n2.val)
                root.left=add(n1.left,n2.left)
                root.right=add(n1.right,n2.right)
                return root
            return n1 or n2
        return add(root1,root2)        
