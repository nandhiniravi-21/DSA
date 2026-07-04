class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            # If found, or if we pass the point where it should be
            if nums[i] >= target:
                return i

        # If target is greater than all elements, insert at the end
        return len(nums)