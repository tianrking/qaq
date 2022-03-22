from typing import List
class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     if not nums:
    #         return 0
    #     new = []

    #     for data in nums:
    #         if data != val:
    #             new.append(data)

    #     # nums = new[::-1]   
        
    #     nums = new[::1]
    #     print(nums)
    #     return len(new)
    
   
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


b = Solution()
g = [1,2,2,4]
print(g)
print(b.removeElement_1(g, 2))
print(g)