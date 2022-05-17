# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        store = []
        current = head
        while current !=None:
            store.append(current.val)
            current = current.next
        store = sorted(set(store))
        head = ListNode()
        new_head = head
        for x in store:
            add = ListNode(x)
            new_head.next = add
            new_head = new_head.next
        return head.next
        
