class Solution:
    # FIX: Renamed function to 'distinctAverages' to match LeetCode's system
    def distinctAverages(self, nums: list[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        # Set up two pointers and a hash set
        left = 0
        right = len(nums) - 1
        averages = set()
        
        # Pair min and max elements iteratively
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            averages.add(avg)
            
            left += 1
            right -= 1
            
        # Return the count of unique averages
        return len(averages)
