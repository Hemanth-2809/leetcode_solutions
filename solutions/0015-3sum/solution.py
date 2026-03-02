class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            x = nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                y = nums[j]+nums[k]
                if  y > -x:
                    k-=1
                elif y < -x:
                    j+=1
                else:
                    res.append([x,nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res


                    

                
        

        
