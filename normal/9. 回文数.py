class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=x
        if x < 0 or (x % 10 == 0 and x != 0) :
            return False
        revertedNumber = 0
        while x >= 1  :
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
        print(revertedNumber)
        return b == revertedNumber
b = Solution()
print(b.isPalindrome(121))