class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i] represents the max floors we can check with 'i' eggs 
        # given the current number of moves.
        dp = [0] * (k + 1)
        moves = 0
        
        # Keep incrementing moves until we can check at least n floors
        while dp[k] < n:
            moves += 1
            
            # Iterate backwards to use values from the previous move iteration
            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs - 1] + dp[eggs] + 1
                
        return moves
