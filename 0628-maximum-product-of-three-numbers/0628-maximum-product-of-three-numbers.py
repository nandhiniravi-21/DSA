class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # Initialize the three largest values
        max1 = max2 = max3 = float('-inf')
        # Initialize the two smallest values
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update the three largest values
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
                
            # Update the two smallest values
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
                
        # Return the maximum of the two possible products
        return max(max1 * max2 * max3, min1 * min2 * max1)
