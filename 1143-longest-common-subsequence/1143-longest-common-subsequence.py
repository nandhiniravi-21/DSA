class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Initialize a 2D array with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the DP table from the ground up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match: take the diagonal value and add 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters mismatch: take the max from top or left cells
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]
