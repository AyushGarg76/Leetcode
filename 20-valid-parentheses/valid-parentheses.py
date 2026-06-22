class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for ch in s: 
            if ch in pairs:
                if not stacks or stacks[-1] != pairs[ch]:
                    return False
                stacks.pop()
            else:
                stacks.append(ch)
        return len(stacks) == 0
