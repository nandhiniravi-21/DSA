class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Case 1: If k == 1, we can only rotate the string.
        # Find the lexicographically smallest rotation.
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
            
        # Case 2: If k > 1, we can achieve any permutation.
        # The smallest possible permutation is the fully sorted string.
        return "".join(sorted(s))
