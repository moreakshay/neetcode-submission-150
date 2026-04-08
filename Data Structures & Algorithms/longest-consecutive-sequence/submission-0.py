class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in nums:
            #check if it is the start of the sequence i.e no previous number
            if num-1 not in num_set:
                length = 1
                #keep checking if the next number exist and then its next i.e checking sequence
                while num + length in num_set:
                    length += 1
                #next number doesn't exist anymore i.e sequence broke
                #so, store the longest sequence found until now.
                longest = max(longest, length)
        return longest