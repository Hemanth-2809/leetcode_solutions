class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dict_colors = {0:0,1:0,2:0}
        for num in nums:
            dict_colors[num]+=1
        index = 0
        for x in [0,1,2]:
            for y in range(dict_colors[x]):
                nums[index] = x
                index +=1
        return nums
        
    


            
        
