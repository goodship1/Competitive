# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = " "
        second = " "
        while l1 != None:
            first+=str(l1.val)
            l1 = l1.next
        first = first[::-1]
        while l2 != None:
            second+=str(l2.val)
            l2 = l2.next
        second = second[::-1]
        res = str(int(second)+int(first))
        res = res[::-1]
        head = ListNode()
        new_head = head
        for x in res:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
