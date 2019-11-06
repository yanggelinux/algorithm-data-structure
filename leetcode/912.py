# -*- coding: utf8 -*-
"""
给定一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""

class Solution(object):
    def sortArray(self, nums):
        """
        归并排序
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:return nums
        mid = len(nums) // 2
        left_nums = self.sortArray(nums[:mid])
        right_nums = self.sortArray(nums[mid:])
        return self.merge(left_nums,right_nums)
    def merge(self,left_nums,right_nums):
        """
        合并子问题
        :param left_nums:
        :param right_nums:
        :return:
        """
        resusts = []
        while 1:
            if left_nums and right_nums:
                if left_nums[0] < right_nums[0]:
                    mim_num,left_nums = left_nums[0],left_nums[1:]
                else:
                    mim_num,right_nums = right_nums[0],right_nums[1:]
            elif left_nums and not right_nums:
                mim_num, left_nums = left_nums[0], left_nums[1:]
            elif right_nums and not left_nums:
                mim_num, right_nums = right_nums[0], right_nums[1:]
            else:break
            resusts.append(mim_num)
        return resusts

if __name__ == '__main__':
    slt = Solution()
    nums = [5,1,1,2,0,0]
    print(slt.sortArray(nums))