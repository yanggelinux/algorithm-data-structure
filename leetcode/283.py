# -*- coding: utf8 -*-



"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution(object):
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
            i+=1
        print(nums)

    def move_zeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        #先把非0的元素方法到对应的位置
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        #把最后的元素全部置为0
        for j in range(count,n):
            nums[j] = 0
        print(nums)

if __name__ == '__main__':
    slt = Solution()
    nums = [0, 1, 0, 3, 12]
    slt.move_zeroes2(nums)