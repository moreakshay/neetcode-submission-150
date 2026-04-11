from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        need = Counter(t) # freq map of t
        window = {} # freq map of window

        required = len(need) # number of distinct characters required
        acquired = 0 # number of distinct characters currently in the window

        left = 0
        
        min_start = 0 # least position to start from to get the answer
        min_len = float("inf") # least distance to cover to get the answer

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1 # populating the freq map of the window

            if c in need and window[c] == need[c]: # if c is in t and if we have satisfied the freq of c that is needed
                acquired += 1 # then add to the number of distinct characters we got until now.

            # shrink condition
            while acquired == required: # Now that we got the answer we need to find the next min answer.
                window_len = right - left + 1
                if window_len < min_len: # store the answer
                    min_len = window_len
                    min_start = left
                
                window[s[left]] -= 1 # shrink the window
                if s[left] in need and window[s[left]] < need[s[left]]:
                    acquired -= 1
                
                left += 1
        
        if min_len == float("inf"):
            return "" # This means s doesn't have the characters needed in t. i.e we never got the answer
        
        return s[min_start: min_start + min_len]