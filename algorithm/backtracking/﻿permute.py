# -*- coding: utf8 -*-

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):

    def __init__(self):
        self.res_list = []

    def backtrack(self,start,nums):
        """
        回溯
        :param start:
        :return:
        """
        n = len(nums)
        if start == n:
            if nums not in self.res_list:
                self.res_list.append(nums[:])
        for i in range(start,n):
            #调换位置
            nums[start],nums[i] = nums[i],nums[start]
            self.backtrack(start+1,nums)
            #恢复状态
            nums[start], nums[i] = nums[i], nums[start]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        self.backtrack(start,nums)
        return self.res_list