from bisect import bisect_left

class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        # Step 1: Group rectangle lengths by their heights (1 to 100)
        height_to_lengths = [[] for _ in range(101)]
        for l, h in rectangles:
            height_to_lengths[h].append(l)
            
        # Step 2: Sort the lengths for each height bucket
        for h in range(101):
            if height_to_lengths[h]:
                height_to_lengths[h].sort()
                
        ans = []
        
        # Step 3: For each point, count containing rectangles using binary search
        for x, y in points:
            count = 0
            # Iterate through all valid heights starting from the point's y-coordinate
            for h in range(y, 101):
                lengths = height_to_lengths[h]
                if lengths:
                    # Find the first index where length >= x
                    idx = bisect_left(lengths, x)
                    count += len(lengths) - idx
            ans.append(count)
            
        return ans
