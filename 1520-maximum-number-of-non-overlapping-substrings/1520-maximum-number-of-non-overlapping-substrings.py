class Solution:
    # FIX: Renamed function to include 'Of' to match LeetCode's system
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Find the first and last occurrence of each character
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}
        
        valid_intervals = []
        
        # Generate and expand intervals for each unique character
        for c in set(s):
            start = first[c]
            end = last[c]
            
            i = start
            is_valid = True
            while i <= end:
                # If a character inside starts before our interval, this interval is invalid
                if first[s[i]] < start:
                    is_valid = False
                    break
                # Expand the end boundary if needed
                end = max(end, last[s[i]])
                i += 1
                
            if is_valid:
                valid_intervals.append([start, end])
                
        # Sort intervals primarily by their end positions
        valid_intervals.sort(key=lambda x: x[1])
        
        # Greedy selection of non-overlapping intervals
        result = []
        prev_end = -1
        
        for start, end in valid_intervals:
            # If the interval does not overlap with the previous one, pick it
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end
                
        return result
