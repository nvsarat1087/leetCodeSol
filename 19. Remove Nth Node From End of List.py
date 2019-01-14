# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        firstP = head
        secondP = head
        prev = None
        
        while n != 0 and firstP is not None:
            firstP = firstP.next
            n = n - 1 
        
        if firstP is None:
            return head.next
        
        while firstP is not None:
            firstP = firstP.next
            prev = secondP
            secondP = secondP.next
            
        
        prev.next = secondP.next
        return head
        
