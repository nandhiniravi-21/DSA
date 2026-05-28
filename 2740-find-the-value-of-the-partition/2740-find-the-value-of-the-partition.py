class Solution:
    # FIX: Renamed function to 'findValueOfPartition' to match LeetCode's system
    def findValueOfPartition(self, nums: list[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        min_val = float('inf')
        
        # Find the smallest difference between adjacent elements
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff < min_val:
                min_val = diff
                
        return min_val
