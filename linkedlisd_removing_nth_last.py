'''
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list
becomes 1->2->3->5.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=1
        c=head
        while(head.next != None):
            length+=1
            head=head.next
        head=c
        r=0
        f=ListNode(0)
        cf=f
        while(head.next != None):
            r+=1
            if(r!=(length-n+1)):
                f.next=ListNode(head.val)
                f=f.next
            head=head.next
            if(n!=1):
                f.next=ListNode(head.val)
            

        return(cf.next)
        
