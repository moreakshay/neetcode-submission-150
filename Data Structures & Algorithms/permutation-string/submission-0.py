class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sfmap, wfmap = [0] * 26, [0] * 26
        left, right = 0, 0
        for c in s1:
            sfmap[ord(c) - ord('a')] += 1
        
        while right < len(s2):
            wfmap[ord(s2[right]) - ord('a')] += 1

            if (right - left + 1) > len(s1):
                wfmap[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            right += 1
            
            if wfmap == sfmap:
                return True

        return False