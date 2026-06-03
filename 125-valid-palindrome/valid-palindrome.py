class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s.strip().lower() 
        cleaned = ''.join([char for char in a if char.isalnum()]) 
        if cleaned == cleaned[::-1]: 
            return True 
        return False