# -*- coding: utf8 -*-


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        暴力法
        :type nums: List[int]
        :rtype: int
        """
        import sys
        n = len(nums)
        if n ==0:return 0
        if n ==1:return nums[0]
        max_res = -sys.maxsize - 1
        for i in range(n):
            for j in range(i,n):
                # print(nums[i:j+1],sum(nums[i:j+1]))
                sum_res = sum(nums[i:j+1])
                if sum_res > max_res:
                    max_res = sum_res
        return max_res
    def maxSubArray2(self, nums):
        """
        动态规划
        动态转移方程 dp[i] = max(nums[i],nums[i] + dp[i-1])
        最大子序和 = 当前元素自身最大，或 包含之前后最大
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = nums[:]
        for i in range(1,n):
            # nums[i] = max(nums[i],nums[i]+nums[i-1])
            dp[i] = max(nums[i],nums[i] + dp[i-1])
        # return max(nums)

        return max(dp)

if __name__ == '__main__':
    slt = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(slt.maxSubArray2(nums))