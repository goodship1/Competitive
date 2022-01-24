# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        store = []
        while current !=None:
            current = current.next#moves down the list
            if current in store:
                return True
            else:
                store.append(current)
        return False
