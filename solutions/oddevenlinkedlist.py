# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        current = head
        index = 1
        while current != None:
            if index%2 == 0:
                even.append(current.val)
            elif index%2!=0:
                odd.append(current.val)
            current = current.next
            index+=1
        
        new_list = odd + even
        head = ListNode()
        new_head = head
        for x in new_list:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
            
