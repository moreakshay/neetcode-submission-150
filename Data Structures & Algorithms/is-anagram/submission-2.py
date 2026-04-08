class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
    
        for idx in range(len(s)):
            s_freq[s[idx]] += 1
            t_freq[t[idx]] += 1
            
        return s_freq == t_freq