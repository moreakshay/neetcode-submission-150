class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We call the helper with the full range of the list
        return self.binary_search_recursive(nums, target, 0, len(nums) - 1)

    def binary_search_recursive(self, nums, target, left, right):
        # Base case: If the range is empty, the target isn't here
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # If target is smaller, search the left side
        if target < nums[mid]:
            return self.binary_search_recursive(nums, target, left, mid - 1)
        
        # If target is larger, search the right side
        else:
            return self.binary_search_recursive(nums, target, mid + 1, right)