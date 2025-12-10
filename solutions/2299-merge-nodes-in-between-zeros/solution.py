# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head.next
        summ = 0
        newlist = ListNode(0)
        tail = newlist
        
        while temp:
            if temp.val == 0:
                tail.next = ListNode(summ)
                tail = tail.next
                summ = 0 
            else:
                summ += temp.val
            temp = temp.next
        return newlist.next

            


        
