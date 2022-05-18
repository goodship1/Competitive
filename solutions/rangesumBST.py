# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        compare = [x for x in range(low,high+1)]
        elements = self.findelements(root)
        res = 0
        for x in elements:
            if x in compare:
                res+=x
        return res
    
    def findelements(self,root):
        store = []
        if root == None:
            return 0
        else:
            if root.left:
                store += self.findelements(root.left)
            store.append(root.val)
            if root.right:
                store+= self.findelements(root.right)
        return store
