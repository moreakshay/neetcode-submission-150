class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        m = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                m = min(m, nums[l])
                break

            n = (l + r) // 2
            m = min(m, nums[n])
            if nums[l] <= nums[n]:
                l = n + 1
            else:
                r = n - 1
        return m
        