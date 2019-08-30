# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
using linked list only
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print('l:',len(lists))
        def merg2(l1,l2):
            l=ListNode(-9999)
            c=l
            while(l1 != None and l2 != None):
                if(l1.val>l2.val):
                    l.next=ListNode(l2.val)
                    l=l.next
                    l2=l2.next
                else:
                    l.next=ListNode(l1.val)
                    l=l.next
                    l1=l1.next
            if(l1 != None):
                l.next=l1
            elif(l2 != None):
                l.next=l2
            
            return(c.next)
        li=ListNode(-9999)
        cl=li
        for i in range(0,len(lists)):
            li=merg2(li,lists[i])
        return(li.next)
'''
# using a normal list to reduce complexity
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
                    
                    
        
