class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        index_map = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_len = 0
        n = len(arr)
        
        for k in range(n):
            for j in range(k):
                # The required previous term to satisfy arr[i] + arr[j] == arr[k]
                target = arr[k] - arr[j]
                
                # Check if target exists and appears strictly before index j
                if target in index_map and index_map[target] < j:
                    i = index_map[target]
                    # Update DP state and fetch previous length (default to 2 if it's the start)
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[(j, k)])
                    
        return max_len if max_len >= 3 else 0
