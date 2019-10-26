# -*- coding: utf8 -*-


"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        回溯的方法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        n = len(nums)
        def helper(i,tmp):
            results.append(tmp)
            for j in range(i,n):
                helper(j+1,tmp+[nums[j]])
        helper(0,[])
        return results

    def subsets2(self, nums):
        """
        迭代的方法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for num in nums:
            subs = []
            for res in results:
                new_res = res + [num]
                subs.append(new_res)
            results = results +  subs
        return results





if __name__ == '__main__':
    slt = Solution()
    nums = [1,2,3]
    print(slt.subsets2(nums))