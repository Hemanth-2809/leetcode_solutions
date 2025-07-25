class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height)-1
        max_area = 0
        for i in range(len(height)):
            area = (p2-p1) * min(height[p1],height[p2])
            if area > max_area:
                max_area = area
            if height[p1]<height[p2]:
                p1 = p1+1
            else:
                p2 = p2-1
        return max_area




