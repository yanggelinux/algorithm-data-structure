# -*- coding: utf8 -*-


"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    def two_sum(self, nums, target):
        """
        暴力法时间复杂度O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    print([i,j])
                    return [i,j]
        else:
            return []

    def two_sum2(self, nums, target):
        """
        一遍哈希表法，时间复杂度O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        map = {}
        for i in range(n):
            a = nums[i]
            b = target - a
            if b in map and map.get(b) != i:
                return [map.get(b), i]
            map[a] = i

    def two_sum3(self, nums, target):
        """
         二遍哈希表法，时间复杂度O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        n = len(nums)
        for i in range(n):
            map[nums[i]] = i

        for j in range(n):
            res = target - nums[j]
            if map.get(res) is not None and j != map[res]:
                return [j,map[res]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 18
    slt = Solution()
    print(slt.two_sum3(nums, target))