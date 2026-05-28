class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Step 1: Combine the total allowed operations
        k = k1 + k2
        
        # Step 2: Create frequency buckets for the absolute differences
        # Max difference possible is 10^5 based on constraints
        MAX_DIFF = 100000
        buckets = [0] * (MAX_DIFF + 1)
        
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            buckets[diff] += 1
            
        # Step 3: Greedily reduce the largest differences down to smaller ones
        for v in range(MAX_DIFF, 0, -1):
            if buckets[v] == 0:
                continue
                
            # If we have enough operations to reduce all elements of value 'v' to 'v-1'
            if k >= buckets[v]:
                k -= buckets[v]
                buckets[v - 1] += buckets[v]
                buckets[v] = 0
            else:
                # We can only reduce 'k' elements of value 'v' to 'v-1'
                buckets[v - 1] += k
                buckets[v] -= k
                k = 0
                break
                
        # Step 4: Calculate the final sum of squared differences
        return sum(count * (v ** 2) for v, count in enumerate(buckets))
