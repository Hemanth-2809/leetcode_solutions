# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        listsol = []
        temp = head.next
        prev = head
        i = 2
        while temp and temp.next:
            if prev.val<temp.val>temp.next.val or prev.val>temp.val<temp.next.val:
                listsol.append(i)
            prev = temp
            temp = temp.next

            i=i+1
        
        if len(listsol)<2:
            return [-1,-1]
        listsoll = []
        for i in range(1,len(listsol)):
            listsoll.append(listsol[i]-listsol[i-1])
        maxx = listsol[-1] - listsol[0]
        
         
        return [min(listsoll),maxx]
        

            

        
