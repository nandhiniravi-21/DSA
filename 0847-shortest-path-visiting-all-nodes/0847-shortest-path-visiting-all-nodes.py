from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        
        # Target state: all n bits are set to 1
        target_mask = (1 << n) - 1
        
        # Queue stores tuples of: (current_node, visited_mask, steps)
        queue = deque()
        # Visited set tracks: (current_node, visited_mask)
        visited = set()
        
        # Initialize BFS by adding every node as a potential starting point
        for i in range(n):
            initial_mask = 1 << i
            queue.append((i, initial_mask, 0))
            visited.add((i, initial_mask))
            
        while queue:
            node, mask, steps = queue.popleft()
            
            # If all nodes have been visited, return the number of steps
            if mask == target_mask:
                return steps
                
            # Travel to all adjacent neighbors
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                
                # Only proceed if this state combination is uniquely new
                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, steps + 1))
                    
        return 0
