class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head:             #if first element is itself = val drop that and update head
            if head.val==val:
                head = head.next
            else:
                break
        node = head
        prev = head         
        while node:
            if node.val == val:
                prev.next = node.next          #bypass element to be removed
            else:
                prev = node                     
            node = node.next
        return head          
