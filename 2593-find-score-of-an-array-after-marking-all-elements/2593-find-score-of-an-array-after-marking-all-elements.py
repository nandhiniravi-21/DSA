class Solution:
    def findScore(self, nums: list[int]) -> int:
        n = len(nums)
        marked = [False] * n
        
        # Sort values while preserving their original index mapping
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        score = 0
        
        for val, idx in sorted_nums:
            if marked[idx]:
                continue
                
            score += val
            marked[idx] = True
            
            # Mark adjacent neighbors if they exist
            if idx > 0:
                marked[idx - 1] = True
            if idx < n - 1:
                marked[idx + 1] = True
                
        return score
