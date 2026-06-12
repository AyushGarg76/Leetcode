class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        required = len(need)
        low = 0
        window = {}
        formed = 0
        min_len = float('inf')

        for high in range(len(s)):
            window[s[high]] = window.get(s[high], 0) + 1
            ch = s[high]

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if high - low + 1 < min_len:
                    min_len = high - low + 1
                    start = low
                low_ch = s[low]
                window[low_ch] -= 1
                if low_ch in need and window[low_ch] < need[low_ch]:
                    formed -= 1
                low += 1
        if min_len == float('inf'):
            return ""
        return s[start:start+min_len]
        
                