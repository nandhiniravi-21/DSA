from collections import Counter

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        # Step 1: A doubled array must have an even number of elements
        if len(changed) % 2 != 0:
            return []
            
        # Step 2: Count frequencies of each number
        counts = Counter(changed)
        
        # Step 3: Sort the array to process elements from smallest to largest
        changed.sort()
        
        original = []
        
        # Step 4: Pair elements greedily
        for x in changed:
            # If x has already been used up as a partner, skip it
            if counts[x] == 0:
                continue
                
            # If we don't have its doubled partner available, it's an invalid layout
            if counts[2 * x] == 0:
                return []
                
            # Valid pair found: append the original number and decrement counts
            original.append(x)
            counts[x] -= 1
            counts[2 * x] -= 1
            
        return original
