Python 3.7.0a2 (v3.7.0a2:f7ac4fe52a, Oct 16 2017, 21:11:18) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        current = head
        # while current is not None: is not necessary
        while current:
            node_next = current.next 
            current.next = pre
            pre = current
            current = node_next
        return pre
        
