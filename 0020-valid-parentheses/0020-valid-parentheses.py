class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # If stack is empty or top item doesn't match, it's invalid
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Successfully matched and removed
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)
                
        # The string is valid only if all opening brackets were cleared out
        return len(stack) == 0
