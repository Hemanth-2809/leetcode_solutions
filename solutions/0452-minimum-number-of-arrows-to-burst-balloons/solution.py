class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points.sort(key=lambda x: x[0])   

        merged = [points[0]]

        for i in range(1, len(points)):
            prev = merged[-1]
            curr = points[i]
            
            if curr[0] <= prev[1]:
                prev[0] = max(prev[0], curr[0])
                prev[1] = min(prev[1], curr[1])
                del merged[-1]
                merged.append(prev)
            else:
                merged.append(curr)

        return len(merged)
