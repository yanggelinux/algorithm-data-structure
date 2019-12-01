# -*- coding: utf8 -*-


"""
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
"""

class Solution(object):

    def __init__(self):

        self.count = 0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i < j and nums[i] > 2*nums[j]:
                    count += 1
        return count
    
    
    def reversePairs2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left_nums = self.reversePairs2(nums[mid:])
        right_nums = self.reversePairs2(nums[:mid])
        return self.merge(left_nums, right_nums)
    
    def merge(self,left_nums,right_nums):
        """
        :param left_nums: 
        :param right_nums: 
        :return: 
        """
        result = []
        while 1:
            if left_nums and right_nums:
                if left_nums[0] > right_nums[0]:
                    min_num, right_nums = right_nums[0], right_nums[1:]
                    self.count += 1
                else:
                    min_num, left_nums = left_nums[0], left_nums[1:]
            elif left_nums and not right_nums:
                min_num, left_nums = left_nums[0], left_nums[1:]
            elif right_nums and not left_nums:
                min_num, right_nums = right_nums[0], right_nums[1:]
            else:
                break
            result.append(min_num)
        return result


if __name__ == '__main__':
    slt = Solution()
    nums = [1,3,2,3,1]
    print(slt.reversePairs2(nums))
    print(slt.count)