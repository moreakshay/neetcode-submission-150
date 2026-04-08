class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        found_vals = []

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complement_map:
                found_vals = [i, complement_map[complement]]
            
            complement_map[num] = i
        
        return sorted(found_vals)


        