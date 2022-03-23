class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        r = 1
        p = 0
        q = 0 
        for i in range(1,n):
            p = q
            q = r
            r = p + q 
        return r

