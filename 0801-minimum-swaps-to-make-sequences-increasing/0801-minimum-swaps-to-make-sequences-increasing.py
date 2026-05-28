class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        
        # Base cases for index 0
        # If we don't swap index 0, it costs 0 swaps.
        # If we do swap index 0, it costs 1 swap.
        keep = 0
        swap = 1
        
        for i in range(1, n):
            next_keep = float('inf')
            next_swap = float('inf')
            
            # Case 1: The arrays are already sorted without swapping current or previous
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                next_keep = keep        # previous wasn't swapped, current isn't swapped
                next_swap = swap + 1    # previous was swapped, current is swapped
                
            # Case 2: The arrays become sorted if we alternate swap states
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                next_keep = min(next_keep, swap)      # previous was swapped, current isn't
                next_swap = min(next_swap, keep + 1)  # previous wasn't swapped, current is
                
            keep = next_keep
            swap = next_swap
            
        return min(keep, swap)
