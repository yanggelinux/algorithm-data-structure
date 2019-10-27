# -*- coding: utf8 -*-

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        n = len(nums)
        def backtrack(start=0):
            if start == n:
                if nums not in results:
                    results.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return results

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        def backtrack(res):
            if len(res) == len(nums):
                results.append(res[:])
            for num in nums:
                if num in res:continue
                res.append(num)
                backtrack(res)
                res.pop()

        backtrack(res=[])
        return results

if __name__ == '__main__':
    slt = Solution()
    nums = [1,1,2]
    print(slt.permuteUnique2(nums))