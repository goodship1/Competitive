# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result  = []#stores the results
        if root !=None:
            result.append(root.val)#store the root value first
            result = result + self.preorderTraversal(root.left)#then left values 
            result = result + self.preorderTraversal(root.right)#then right values
        return result#return the array
