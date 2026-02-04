class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        def neighbours(curr_state):
            res = []
            for i in range(4):
                digit = str((int(curr_state[i]) + 1) % 10)
                res.append(curr_state[:i] + digit + curr_state[i+1:])
                digit = str((int(curr_state[i]) - 1 + 10) % 10)
                res.append(curr_state[:i] + digit + curr_state[i+1:])
            return res

        q = deque([("0000",0)])
        visited = set(deadends)
        while q:
            curr_state,turns = q.popleft()
            if curr_state == target:
                return turns
            for each in neighbours(curr_state):
                if each not in visited:
                    visited.add(each)
                    q.append((each,turns+1))
        return -1

        
