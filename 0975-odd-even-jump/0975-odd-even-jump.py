class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)
        
        # Helper function using a monotonic stack to find the next valid jump index
        def make_jumps(sorted_indices):
            next_jumps = [-1] * n
            stack = []
            for idx in sorted_indices:
                while stack and stack[-1] < idx:
                    next_jumps[stack.pop()] = idx
                stack.append(idx)
            return next_jumps

        # 1. Generate next odd jumps (sorted ascending by value, then ascending by index)
        sorted_odd = sorted(range(n), key=lambda i: (arr[i], i))
        next_odd = make_jumps(sorted_odd)
        
        # 2. Generate next even jumps (sorted descending by value, then ascending by index)
        sorted_even = sorted(range(n), key=lambda i: (-arr[i], i))
        next_even = make_jumps(sorted_even)
        
        # 3. Dynamic Programming arrays
        odd = [False] * n
        even = [False] * n
        
        # Base Case: The last element is always reachable from itself
        odd[n - 1] = True
        even[n - 1] = True
        
        # Process from right to left
        for i in range(n - 2, -1, -1):
            if next_odd[i] != -1:
                odd[i] = even[next_odd[i]]
            if next_even[i] != -1:
                even[i] = odd[next_even[i]]
                
        # The first jump is always odd-numbered
        return sum(odd)
