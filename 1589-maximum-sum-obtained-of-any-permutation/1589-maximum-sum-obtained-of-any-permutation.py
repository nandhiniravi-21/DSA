class Solution:
    # FIX: Renamed function to 'maxSumRangeQuery' to match LeetCode's system
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # Initialize difference array
        count = [0] * (n + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
            
        # Reconstruct frequencies using prefix sum
        for i in range(1, n):
            count[i] += count[i - 1]
            
        # Pop the extra out-of-bounds tracking index
        count.pop()
        
        # Sort both arrays to pair largest numbers with highest frequencies
        count.sort()
        nums.sort()
        
        # Sum up the optimized products
        total_sum = sum(c * num for c, num in zip(count, nums))
        
        return total_sum % MOD
