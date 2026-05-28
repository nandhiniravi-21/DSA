class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left = right = 0
        
        # Pass 1: Scan Left to Right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                # Reset counters if we have too many closing brackets
                left = right = 0
                
        left = right = 0
        
        # Pass 2: Scan Right to Left
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                # Reset counters if we have too many opening brackets
                left = right = 0
                
        return max_len
