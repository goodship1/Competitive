# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        while current!=None:
            stack.append(current.val)
            current = current.next
        palindome =  stack[::-1]
        return palindome == stack
