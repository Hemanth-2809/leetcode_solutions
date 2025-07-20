class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brac_dict = {"]":"[","}":"{",")":"("}
        if  s[0] in [']','}',')']:
            return False
        
        for i in range(len(s)):
            
            if s[i] in ['[', '(', '{']:
                stack.append(s[i])
            else:
                if stack and brac_dict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack)==0:
            return True
        else :
            return False
                


        
