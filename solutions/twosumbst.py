# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = self.inorder(root)
        addends = {}
        for i in range(len(s)):
            if k - s[i] in addends:
                return [addends[k - s[i]],i]
            else:
                addends[s[i]]=i
        
    def inorder(self,root):
        if not root:
            return []
        
        store = [root.val]
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return store + left + right
        
