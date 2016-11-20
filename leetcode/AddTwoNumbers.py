# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nCarryOver = 0
        nVal       = 0
        result     = curNode = None
        while l1 and l2 :
            nVal = l1.val + l2.val + nCarryOver
            if nVal >=10 :
                nVal-=10
                nCarryOver = 1
            else:
                nCarryOver = 0
            
            if result==None:
                result = curNode = ListNode(nVal)
            else:
                curNode.next = ListNode(nVal)
                curNode = curNode.next
            l1  = l1.next
            l2  = l2.next
        
        while l1:
            nVal = l1.val + nCarryOver
            if nVal  >=10:
                nVal -=10
                nCarryOver = 1
            else:
                nCarryOver = 0
            
            if result==None:
                result = curNode = ListNode(nVal)
            else:
                curNode.next = ListNode(nVal)
                curNode = curNode.next
            l1 = l1.next
        
        while l2:
            nVal = l2.val + nCarryOver
            if nVal >=10:
                nVal -=10
                nCarryOver = 1
            else:
                nCarryOver = 0
            
            if result==None:
                result = curNode = ListNode(nVal)
            else:
                curNode.next = ListNode(nVal)
                curNode = curNode.next
            l2 = l2.next
            
        if l1==None and l2==None and nCarryOver==1 :
            curNode.next = ListNode(nCarryOver)
            
        return result
            
            
