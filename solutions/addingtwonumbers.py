# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = " "
        second_num = " "
        while l1 !=None:
            first_num +=str(l1.val)
            l1 = l1.next
        while l2!=None:
            second_num+=str(l2.val)
            l2 = l2.next
        res = int(first_num)+ int(second_num)
        store = []
        for x in str(res):
            store.append(int(x))
        
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = add
        return head.next
            
        
