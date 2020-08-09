# -*- coding: utf8 -*-

"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        暴力：超时
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        if n == 0: return count
        for i in range(n):
            sum = 0
            j = i
            while j < n:
                sum += nums[j]
                j += 1
                if sum == k: count += 1
        return count

    def subarraySum2(self, nums, k):
        """
        优化
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = {0: 1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if ((sum - k) in hash):
                count += hash[sum - k]
            if (sum in hash):
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count


if __name__ == '__main__':
    slt = Solution()
    nums = [28,54,7,-70,22,65,-6]
    k = 100
    print(slt.subarraySum(nums, k))
