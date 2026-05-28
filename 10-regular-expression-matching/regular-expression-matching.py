class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Base Case: Deal with patterns that can match an empty string (like "a*", "a*b*")
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Case 1: Match 0 times (ignore the character and the '*')
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Match 1 or more times (if preceding character matches s[i-1])
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
                else:
                    # Normal character or '.' match
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                        
        return dp[m][n]
