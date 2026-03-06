class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reach = 0
        min_steps = 0
        curr = 0
       

        for i in range(len(nums)-1):
            
            max_reach = max(max_reach, i + nums[i])
            if i == curr:
                min_steps +=1
                curr = max_reach



        return min_steps
        
