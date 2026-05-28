class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        # Step 1: Sort the array to group close values together
        nums.sort()
        
        result = []
        n = len(nums)
        
        # Step 2: Slice the array into chunks of 3 elements
        for i in range(0, n, 3):
            # Because the chunk is sorted, the max diff is always (last - first)
            if nums[i + 2] - nums[i] > k:
                return []
                
            result.append([nums[i], nums[i + 1], nums[i + 2]])
            
        return result
