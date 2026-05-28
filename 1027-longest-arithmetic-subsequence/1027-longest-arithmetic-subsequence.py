class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i] will store a dict of {difference: length_of_sequence}
        dp = [{} for _ in range(n)]
        max_len = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # If the difference exists at index j, extend it. Otherwise, start a sequence of length 2.
                dp[i][diff] = dp[j].get(diff, 1) + 1
                
                # Update our global maximum length
                max_len = max(max_len, dp[i][diff])
                
        return max_len
