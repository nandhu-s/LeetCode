"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node', ans: List =None) -> List[int]:
        if not root:
            return ans
        if ans==None:
            ans=[]
        ans.append(root.val)
        for n in root.children:
            self.preorder(n, ans)
        return(ans)
