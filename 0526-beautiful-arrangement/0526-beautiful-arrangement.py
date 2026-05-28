class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        count = 0
        
        def backtrack(pos):
            nonlocal count
            if pos > n:
                count += 1
                return
            
            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    backtrack(pos + 1)
                    visited[num] = False  # Undo the choice
                    
        backtrack(1)
        return count
