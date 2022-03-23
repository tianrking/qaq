class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        r = 1
        p = 0
        q = 1 
        for i in range(1,n):
            p = q
            q = r
            r = p + q 
        return r


b = Solution()
print(b.climbStairs(3))