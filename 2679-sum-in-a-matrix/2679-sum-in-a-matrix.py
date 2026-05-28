class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        # Step 1: Sort each row in ascending order
        for row in nums:
            row.sort()
            
        score = 0
        
        # Step 2 & 3: zip(*nums) transposes the matrix to iterate column by column
        for col in zip(*nums):
            # Identify the highest number amongst all those removed in this step
            score += max(col)
            
        return score
