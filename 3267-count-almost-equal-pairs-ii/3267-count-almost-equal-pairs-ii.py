from collections import Counter

class Solution:
    def countPairs(self, nums: list[int]) -> int:
        # Global frequency map to track previous numbers
        counts = Counter()
        ans = 0
        
        # Helper to generate all unique integers reachable after 0, 1, or 2 swaps
        def get_all_variants(num: int) -> set[int]:
            # Pad to 7 digits to cleanly handle any leading zero operations
            s = list(f"{num:07d}")
            variants = {num}
            
            # Step 1: Generate 1-swap states
            first_swap_states = []
            for i in range(7):
                for j in range(i + 1, 7):
                    if s[i] != s[j]:
                        s[i], s[j] = s[j], s[i]
                        v = int("".join(s))
                        variants.add(v)
                        first_swap_states.append((v, list(s)))
                        s[i], s[j] = s[j], s[i] # Backtrack
                        
            # Step 2: Generate 2-swap states branching off from 1-swap states
            for _, state in first_swap_states:
                for i in range(7):
                    for j in range(i + 1, 7):
                        if state[i] != state[j]:
                            state[i], state[j] = state[j], state[i]
                            variants.add(int("".join(state)))
                            state[i], state[j] = state[j], state[i] # Backtrack
                            
            return variants

        # Process each number sequentially
        for num in nums:
            # Find all unique targets this number can match
            possible_matches = get_all_variants(num)
            
            # If any previous number matches a variant, it forms a valid pair
            for variant in possible_matches:
                if variant in counts:
                    ans += counts[variant]
                    
            # Register the original unswapped number into our history
            counts[num] += 1
            
        return ans
