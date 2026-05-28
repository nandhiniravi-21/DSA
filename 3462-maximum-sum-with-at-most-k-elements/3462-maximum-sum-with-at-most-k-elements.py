class Solution:
    # FIX: Renamed function to 'maxSum' to match LeetCode's system
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        candidate_pool = []
        
        # Keep only the largest allowed elements from each row
        for row, limit in zip(grid, limits):
            if limit > 0:
                # Sort row in descending order and take the top 'limit' elements
                row.sort(reverse=True)
                candidate_pool.extend(row[:limit])
                
        # Sort the global pool of valid elements in descending order
        candidate_pool.sort(reverse=True)
        
        # Return the sum of the top 'k' largest valid elements
        return sum(candidate_pool[:k])
