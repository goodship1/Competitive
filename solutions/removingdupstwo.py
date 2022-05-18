# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        current = head
        while current!=None:
            store.append(current.val)
            current = current.next
        count = Counter(store)
        store = [x for x,y in count.items() if y==1]
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = add
        return head.next
        
