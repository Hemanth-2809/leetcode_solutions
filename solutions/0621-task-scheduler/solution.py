import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxheap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(maxheap)

        time = 0

        while maxheap:
            temp = []
            cycle = n + 1

            while cycle > 0 and maxheap:
                freq, task = heapq.heappop(maxheap)
                time += 1          
                if freq + 1 < 0:   
                    temp.append((freq + 1, task))
                cycle -= 1
            for item in temp:
                heapq.heappush(maxheap, item)

            if maxheap:
                time += cycle

        return time

