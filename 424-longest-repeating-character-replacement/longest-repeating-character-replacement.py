class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low = 0 
        high = 0
        ans = 0
        freq = {}
        max_count = 0
        result = 0
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high], 0) + 1
            length = high - low + 1
            max_count = max(max_count, freq[s[high]])
            diff = length - max_count
            while diff > k:
                freq[s[low]] -= 1
                low += 1
                max_count = max(max_count, freq[s[high]])
                length = high - low + 1
                diff = length - max_count
            length = high - low + 1
            result = max(result, length)
        return result