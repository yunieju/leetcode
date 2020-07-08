# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # step 1. calculate the length of the linked list
        temp = head
        
        # make a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        
        # step 2. find the node need to be deleted
        temp = dummy # reset temp to the head
        for i in range(1, length-n):
            temp = temp.next
        temp.next = (temp.next.next if temp.next.next else None)
        
        return dummy.next         
