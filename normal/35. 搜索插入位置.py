from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        # 在 [low, high] 找 target
        while low <= high:

            mid = (low + high) // 2

            # 如果 target 找到，直接返回位置
            if nums[mid] == target:
                return mid
            # 如果 target 大于中间数，则 target 可能在右区间
            # 在 [mid + 1, left] 中找
            elif nums[mid] < target:
                low = mid + 1
            # 如果 target 小于中间数，则 target 可能在左区间
            # 在 [left, mid -1] 中找
            else:
                high = mid - 1
        
        # 如果在数组中没找到，则返回需要插入数值的位置
        return high + 1

b = Solution()
print(b.searchInsert([1,2,333,554], 7))