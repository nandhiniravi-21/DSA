class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        # Extract and sort even indices in ascending order
        even_sorted = sorted(nums[::2])
        
        # Extract and sort odd indices in descending order
        odd_sorted = sorted(nums[1::2], reverse=True)
        
        # Interleave the sorted segments back into the original slots
        nums[::2] = even_sorted
        nums[1::2] = odd_sorted
        
        return nums
