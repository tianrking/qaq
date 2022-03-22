from typing import List
class Solution:
    
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:

        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
    
    @staticmethod
    def removeDuplicates_2(nums: List[int]) -> List[int]:
        return list(set(nums))

a = Solution.removeDuplicates_2([1,2,1 ,2,3,3])
print(a)