# -*- coding: utf8 -*-


"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

思路：而为数组，变为一维数组，然后用二分查找
"""
class Solution(object):

    def binary_search(self,nums,target):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        if not nums:return False
        low,high = 0,len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums = []
        for mat in matrix:
            nums.extend(mat)
        return self.binary_search(nums,target)


if __name__ == '__main__':
    slt = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 10
    print(slt.searchMatrix(matrix,target))
