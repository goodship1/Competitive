# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        store = []
        current = head
        while current != None:
            store.append(current.val)
            current = current.next
        if store == []:
            return head
        
        list_len =  len(store)
        k =  k%list_len
        if k==0:
            return head
        current = head
        for x in range(list_len-k):
            curr = current
            current = curr.next
        new_current = current
        curr.next = None
        while current.next:
            current = current.next
        current.next = head
        return new_current
            
        
