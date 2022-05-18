class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        
        self.traverse(root, nodes)
        
        return len(nodes) == len(set(nodes)) and nodes == sorted(nodes)
    
    def traverse(self, root: Optional[TreeNode], nodes: List[int]):
        if root:            
            self.traverse(root.left, nodes)
            nodes.append(root.val)
            self.traverse(root.right, nodes)
