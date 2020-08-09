# -*- coding: utf8 -*-


"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] == target:
                i = mid + 1
                j = mid - 1
                while i < n:
                    if nums[i] == nums[mid]:
                        i += 1
                    else:
                        break
                while j >= 0:
                    if nums[j] == nums[mid]:
                        j -= 1
                    else:
                        break
                return [j + 1, i - 1]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]


if __name__ == '__main__':
    slt = Solution()
    nums = [1, 1, 2]
    target = 1
    print(slt.searchRange(nums, target))
