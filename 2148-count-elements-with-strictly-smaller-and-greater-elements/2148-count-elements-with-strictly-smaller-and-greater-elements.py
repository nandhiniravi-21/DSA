class Solution:
    def countElements(self, nums: list[int]) -> int:
        # Find the absolute minimum and maximum values in the array
        min_val = min(nums)
        max_val = max(nums)
        
        # Count elements that are strictly between the minimum and maximum
        return sum(1 for x in nums if min_val < x < max_val)
