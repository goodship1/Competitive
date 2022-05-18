# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        store = []
        if root == None:
            return []
        else:
            if root.left:
                store += self.inorderTraversal(root.left)
            store.append(root.val)
            if root.right:
                store+=self.inorderTraversal(root.right)
        return store
