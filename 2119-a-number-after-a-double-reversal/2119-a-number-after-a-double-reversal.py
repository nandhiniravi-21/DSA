class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # True if num is 0, or if the last digit is not 0
        return num == 0 or num % 10 != 0
