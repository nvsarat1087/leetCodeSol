# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        self.addRec(l1,l2,0,head)
        return head.next
        
    def addRec(self,l1,l2,carry,head):
        if l1 is None and l2 is None:
            if carry == 0:
                return
            else:
                head.next =  ListNode(1) 
                return
                
             
        if l1 is None:
            if carry == 0:
                head.next = l2
            else:
                if l2.val+carry <= 9:
                    head.next =  ListNode(l2.val+carry) 
                    head.next.next = l2.next
                else:
                    head.next =  ListNode((l2.val+carry)%10) 
                    
                    self.addRec(l1,l2.next,1,head.next)
            return    
        if l2 is None:
            if carry == 0:
                head.next = l1
            else:
                if l1.val+carry <= 9:
                    head.next =  ListNode(l1.val+carry) 
                    head.next.next = l1.next
                else:
                    head.next =  ListNode((l1.val+carry)%10) 
                    
                    self.addRec(l1.next,l2,1,head.next)
            return    
        
        if l1.val+l2.val+carry <= 9:
                
                head.next = ListNode(l1.val+l2.val+carry)
                self.addRec(l1.next,l2.next,0,head.next)
                
        else:
                print(l1.val,l2.val)
                head.next = ListNode((l1.val+l2.val+carry)%10)
                self.addRec(l1.next,l2.next,1,head.next)  
        return
        
        
    
    
    
    
