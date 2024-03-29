# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root):
            x=self.maxDepth(root.left)
            y=self.maxDepth(root.right)
            if(x>y):
                return x+1
            else:
                return y+1
        return 0