# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head#current assigned to head
        unique = []#storage of elements
        while current !=None:
            if current not in unique:
                unique.append(current)#stores current vals
                current = current.next#moves current 
            else:
                return current
        return None
        
