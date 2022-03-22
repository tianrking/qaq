from typing import List
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        x = len(haystack) 
        y = len(needle)
        if y==0 or haystack == needle :
            return 0
 
        for i in range(0,x-y+1):
            if haystack[i:i+y] == needle:
                return i

        return -1
b = Solution()
print(b.strStr("abbc", "c"))