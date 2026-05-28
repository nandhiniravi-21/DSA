from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        diagonals = defaultdict(list)
        
        # Step 1: Group all elements by their diagonal identifier (i - j)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
                
        # Step 2 & 3: Sort each diagonal according to its position rule
        for diff, values in diagonals.items():
            if diff >= 0:
                # Bottom-left triangle + middle diagonal: Non-increasing (descending)
                values.sort(reverse=True)
            else:
                # Top-right triangle: Non-decreasing (ascending)
                values.sort()
                
        # Step 4: Rebuild the grid by popping sorted values back into place
        # Reversing the lists allows us to pop(0) efficiently or pop() from the end
        for diff in diagonals:
            diagonals[diff].reverse() # Reverse so we can pop from the back efficiently
            
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop()
                
        return grid
