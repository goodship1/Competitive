# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        elements =  self.findelements(root)
        count = Counter(elements)
        max_count = max(count.values())
        l = [x for x,y in countj == max_val.items() if y== max_count ]
        return l
    
    def findelements(self, root: Optional[TreeNode]) -> List[int]:
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
        
        
