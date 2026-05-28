from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        # Convert the 2D board into a 1D string
        start_state = "".join(str(num) for row in board for num in row)
        target = "123450"
        
        # 1D index mapping for 4-directional moves on a 2x3 grid
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS Setup: queue stores (current_state, moves)
        queue = deque([(start_state, 0)])
        visited = {start_state}
        
        while queue:
            state, moves = queue.popleft()
            
            # If target reached, return current move count
            if state == target:
                return moves
            
            # Find the position of the empty tile '0'
            zero_idx = state.index('0')
            
            # Generate all next valid states
            for next_idx in neighbors[zero_idx]:
                # Convert string to list to perform the swap
                state_list = list(state)
                state_list[zero_idx], state_list[next_idx] = state_list[next_idx], state_list[zero_idx]
                next_state = "".join(state_list)
                
                # If the new state hasn't been seen, add it to the queue
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
                    
        return -1
