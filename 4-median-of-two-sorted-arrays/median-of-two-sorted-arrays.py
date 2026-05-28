class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        # ensure A is smaller
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total_left = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2   # cut in A
            j = total_left - i        # cut in B

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            # correct partition
            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return float(max(A_left, B_left))

            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1