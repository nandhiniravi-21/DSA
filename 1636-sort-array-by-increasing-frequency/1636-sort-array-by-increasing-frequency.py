from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # 1. Count the frequency of each number
        counts = Counter(nums)
        
        # 2. Sort the array using a custom key tuple: (frequency, -value)
        #    This sorts by frequency ascending, then by value descending.
        nums.sort(key=lambda x: (counts[x], -x))
        
        return nums
