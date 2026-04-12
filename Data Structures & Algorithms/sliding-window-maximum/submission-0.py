from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []

        result = []
        # holds value in decreasing order eg: 7, 5, 1...
        window = deque() #data structure that can remove value from star and end

        for right, value in enumerate(nums):
           
           # Remove the left most element of the previous window
            while window and window[0] <= right - k:
               window.popleft()

            # Remove the values that are lesser than current to maintain decreasing order
            while window and nums[window[-1]] <= value:
               window.pop()

            window.append(right)

            # only append to the result after the window has grown to k size
            if right >= k - 1: 
                result.append(nums[window[0]])
        
        return result

