class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        vol = 0
        while left < right:
            left_wall = heights[left]
            right_wall = heights[right]
            cur_vol = min(left_wall, right_wall) * (right - left)
            vol = max(vol, cur_vol)
            if left_wall < right_wall:
                left += 1 
            elif right_wall < left_wall: 
                right -= 1
            else: 
                left += 1
                right -= 1
        
        return vol

