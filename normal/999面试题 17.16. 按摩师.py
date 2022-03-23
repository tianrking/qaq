# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
# 在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
# 给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1
        
        return max(dp0, dp1)


    def massage_2(self, nums: List[int]) -> int:

        not_choose = 0  # 没选的时候最大的情况
        choose = 0      # 选了之后最大的情况

        for item in nums:
            not_choose, choose = max(not_choose, choose), max(not_choose+item, choose)
        
        return max(not_choose, choose)
