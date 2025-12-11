# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        kthnode = head 
        i = 1
        while kthnode:
            if i == n:
                break
            else:
                kthnode = kthnode.next
                i+=1
        dumm = ListNode(0)
        dumm.next = head
        prev = dumm
        temp = head
        while kthnode and kthnode.next:
                prev = prev.next
                temp = temp.next
                kthnode = kthnode.next
        prev.next = temp.next
        return dumm.next
            

        
