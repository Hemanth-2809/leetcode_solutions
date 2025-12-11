# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(add):
            curr = add
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        

        temp1 = reverse(head)
        prev = temp1
        temp = temp1.next
        currmax = prev.val
        while temp:
            if temp.val >= currmax:
                currmax = temp.val
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp = temp.next
        return reverse(temp1)
         


        
    
