class Solution:
    def thirdMax(self, nums):
        uni = set(nums)
        s = sorted(uni, reverse=True)

        if len(s) >= 3:
            return s[2]
        else:
            return s[0]