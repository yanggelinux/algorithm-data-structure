# -*- coding: utf8 -*-


"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

class Solution(object):

    def binary_search(self,nums,target):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        low,high = 0 ,len(nums)-1
        while low <=high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return None
    def find_rotate_index(self,nums):
        """
        二分法查找分割点
        :param nums:
        :return:
        """
        if len(nums) <=1:
            return 0
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[mid-1]:
                return mid
            else:
                if nums[mid] < nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return -1
        splitx = self.find_rotate_index(nums)
        nums1 = nums[0:splitx]
        nums2 = nums[splitx:]
        res1 = self.binary_search(nums1,target)
        res2 = self.binary_search(nums2,target)
        if res1 is None and res2 is None:
            return -1
        if res1 is not None:
            return res1
        if res2 is not None:
            return splitx + res2



if __name__ == '__main__':
    slt = Solution()
    # nums = [4, 5, 6, 7,0,1, 2]
    nums = [6,7,8,1,2,3,4,5]
    # nums = [3,4,5,1,2]
    target = 6
    print(slt.search(nums,target))
    # print(slt.find_rotate_index(nums))
