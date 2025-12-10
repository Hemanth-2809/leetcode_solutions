# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        nodea_1 = None
        nodeaplus1 =None
        curr = list1
        i =0 
        while curr:
            
            if i == a-1:
                nodea_1 = curr
            if i == b+1:
                nodeaplus1 = curr
            curr = curr.next
            i = i+1
        nodea_1.next = list2
        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = nodeaplus1


        return list1
        



        
