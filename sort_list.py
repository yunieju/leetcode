# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(head2)
        return self.merge(l,r)

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        prev.next = l1 or l2
        return dummy.next
            
        
        
        
