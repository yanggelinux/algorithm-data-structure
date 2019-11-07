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
    def permute(self, nums):
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
                # 状态回到之前
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return results


if __name__ == '__main__':
    slt = Solution()
    nums = [1, 1, 2, 3]
    print(slt.permute(nums))
