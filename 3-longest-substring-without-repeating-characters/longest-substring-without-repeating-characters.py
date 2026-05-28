class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the last seen index of each character
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate inside our current window
            if current_char in char_map and char_map[current_char] >= left:
                # Move the left pointer past the previous occurrence
                left = char_map[current_char] + 1
                
            # Update the character's last seen position
            char_map[current_char] = right
            
            # Calculate the current window size and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len
