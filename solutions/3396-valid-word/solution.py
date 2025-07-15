class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        
        if not word.isalnum():
            return False
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            
        if any(char in vowels for char in word):
            if any(char.isalpha() and char not in vowels for char in word):
                return True
                
            else:
                return False
        else:
            return False

