class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, maxf = 0, 0
        left = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            maxf = max(maxf, char_count[s[right]])
            while (right - left + 1) - maxf > k:
                char_count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest