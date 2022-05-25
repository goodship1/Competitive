# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        store = sorted([])
        while head:
            store.append(head.val)
            head = head.next
        
        def helper(store):
            if not store:
                return None
            mid = len(store)//2
            root = TreeNode(store[mid])
            root.left = helper(store[:mid])
            root.right = helper(store[mid+1:])
            return root
        return helper(store)
            
