class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
            
        start, end = 0, 0
        
        # Helper function to expand outward from a given center
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the valid palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes, center is a single character
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindromes, center is between two characters
            len2 = expand_around_center(i, i + 1)
            
            # Find the maximum length between both expansion types
            max_len = max(len1, len2)
            
            # If a longer palindrome is found, update the boundaries
            if max_len > (end - start):
                # Calculate the new start and end indices
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
