# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        head = res
        cf = 0
        
        while l1 or l2 or cf:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            val = val1 + val2 + cf
            
            cf = val // 10
            val = val % 10
            
            res.next = ListNode(val)
            res = res.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return (head.next if head.val == 0 else head)
           
