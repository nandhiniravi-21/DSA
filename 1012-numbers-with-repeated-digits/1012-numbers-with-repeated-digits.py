import math

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # Convert n to a list of digits
        digits = [int(d) for d in str(n)]
        L = len(digits)
        
        # 1. Count numbers with unique digits that have fewer digits than L
        unique_count = 0
        for d in range(1, L):
            # First digit has 9 choices (1-9), remaining (d-1) positions choose from 9 digits
            unique_count += 9 * math.perm(9, d - 1)
            
        # 2. Count numbers with unique digits that have exactly L digits
        visited = set()
        for i, digit in enumerate(digits):
            # For the first position, start from 1. For later positions, start from 0.
            start = 1 if i == 0 else 0
            
            for choice in range(start, digit):
                if choice not in visited:
                    # Choose remaining positions from the remaining available unique digits
                    unique_count += math.perm(10 - (i + 1), L - 1 - i)
            
            # If the current digit of n was already used, we cannot form a unique prefix of n
            if digit in visited:
                break
            visited.add(digit)
        else:
            # If the loop finishes without breaking, n itself is a unique-digit number
            unique_count += 1
            
        # Total numbers with repeated digits = Total numbers - Unique digit numbers
        return n - unique_count
