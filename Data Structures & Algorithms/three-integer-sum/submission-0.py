class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        for anchor in range(len(nums)):
            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            left = anchor + 1
            right = len(nums) - 1
            while left < right :
                sum = nums[left] + nums[anchor] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0: 
                    right -= 1
                else:
                    ans.append([nums[left], nums[anchor], nums[right]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and  nums[right] == nums[right + 1]:
                        right -= 1
        return ans
            