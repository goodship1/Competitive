# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.right==None and root.left == None:
            return root.val == targetSum
        find  = targetSum - root.val
        return self.hasPathSum(root.left,find) or self.hasPathSum(root.right,find)
