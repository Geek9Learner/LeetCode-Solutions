# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return
        '''moving to left node untill it becomes null while appending the left node to nodeList. then start popping the nodelist and append value to element and move towards right subtree.'''
        nodeList=[];element=[]
        current=root
        while(True):
            if(current is not None):
                nodeList.append(current)
                current=current.left
            elif(current is None and len(nodeList)>0):
                current=nodeList.pop()
                element.append(current.val)
                current=current.right
            else:
                break
        return element
                