class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = 0
        max2 = 0
        
        # Find the two largest numbers in a single pass
        for n in nums:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2:
                max2 = n
                
        return (max1 - 1) * (max2 - 1)
