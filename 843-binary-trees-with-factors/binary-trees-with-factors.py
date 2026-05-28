class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        
        # dp map tracks: {value: number_of_valid_trees_with_this_root}
        dp = {x: 1 for x in arr}
        
        for i, root in enumerate(arr):
            for j in range(i):
                left = arr[j]
                
                # Performance optimization: if left * left > root, 
                # no subsequent elements can be valid factors
                if left * left > root:
                    break
                
                # Check if 'left' is a valid factor of 'root'
                if root % left == 0:
                    right = root // left
                    
                    # Ensure the matching 'right' factor exists in our array
                    if right in dp:
                        if left == right:
                            dp[root] += dp[left] * dp[right]
                        else:
                            # Multiply by 2 because left and right children can be swapped
                            dp[root] += dp[left] * dp[right] * 2
                            
                        dp[root] %= MOD
                        
        # The total number of trees is the sum of all individual root trees
        return sum(dp.values()) % MOD
