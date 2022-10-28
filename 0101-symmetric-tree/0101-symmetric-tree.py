# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        nodeList = [root, root]
        
        while nodeList:
            node1, node2 = nodeList.pop(), nodeList.pop()
            
            if(not node1 and not node2):
                continue
            if(not node1 or not node2):
                return False
            if(node1.val != node2.val):
                return False
            
            nodeList.append(node1.left)
            nodeList.append(node2.right)
            
            nodeList.append(node1.right)
            nodeList.append(node2.left)
            
        
        return True