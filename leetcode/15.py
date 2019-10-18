# -*- coding: utf8 -*-


"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res_list.append([nums[i], nums[j], nums[k]])
        print(res_list)
        return res_list

    def three_sum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res_list = []
        map = {}
        for i in range(n):
            map[nums[i]] = i
        print(map)
        for j in range(n):
            for k in range(j+1,n):
                res = - (nums[j] + nums[k])
                if map.get(res) is not None and res != nums[j] != nums[k]:
                    res_list.append([res,nums[j],nums[k]])
        print(res_list)

        for res in res_list:



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    slt = Solution()
    slt.three_sum2(nums)
