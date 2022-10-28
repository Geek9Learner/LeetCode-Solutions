# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return
        '''Idea: Each time inserting node to a list and poping their corresponding value into element list'''
        nodeList=[];element=[]
        nodeList.append(root)
        while(len(nodeList)>0):
            temp=nodeList.pop()
            element.append(temp.val)
            if(temp.right is not None):
                nodeList.append(temp.right)
            if(temp.left is not None):
                nodeList.append(temp.left) 
        return element
        
      