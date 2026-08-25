class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        available = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for ch in text:
            if ch in available:
                available[ch] += 1

        required = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }

        return min(
            available["b"] // required["b"],
            available["a"] // required["a"],
            available["l"] // required["l"],
            available["o"] // required["o"],
            available["n"] // required["n"]
        )