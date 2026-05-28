class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Define Roman numeral values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Step 2 & 3: Iterate through the string except the last character
        for i in range(n - 1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                # Subtractive case: e.g., IV where 1 < 5
                total -= roman_map[s[i]]
            else:
                # Normal additive case
                total += roman_map[s[i]]
                
        # Step 4: Always add the last character's value
        total += roman_map[s[-1]]
        
        return total
