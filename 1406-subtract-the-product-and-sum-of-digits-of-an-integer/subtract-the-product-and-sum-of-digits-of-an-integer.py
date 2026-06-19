class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        pro = 1

        while n > 0:
            digit = n % 10
            add += digit
            pro *= digit
            n //= 10

        return pro - add