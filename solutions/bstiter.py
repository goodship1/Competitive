# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.store = []
        self.inorder(root)
        self.curr =  0
    
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.store.append(root)
            self.inorder(root.right)

    def next(self) -> int:
        current = self.store[self.curr]
        self.curr +=1
        return current.val
        
        

    def hasNext(self) -> bool:
        return len(self.store) > self.curr
        
