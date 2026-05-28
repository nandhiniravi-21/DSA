class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        # dp[r] stores the maximum sum that has a remainder of 'r' when divided by 3
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            # Create a copy of the current dp array to find transitions
            next_dp = list(dp)
            
            for current_sum in dp:
                if current_sum != float('-inf'):
                    new_sum = current_sum + num
                    remainder = new_sum % 3
                    # Update the index corresponding to the new remainder
                    next_dp[remainder] = max(next_dp[remainder], new_sum)
            
            dp = next_dp
            
        return dp[0]
