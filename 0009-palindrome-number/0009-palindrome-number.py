class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        while x>0:
            rev=rev*10+x%10
            x//=10
        return True if rev==temp else False
        