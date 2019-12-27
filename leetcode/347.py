# -*- coding: utf8 -*-


"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res_list = []
        if not nums: return res_list
        if len(nums) <= k: return list(set(nums))
        sm = {}
        for num in nums:
            if sm.get(num) is None:
                sm[num] = 1
            else:
                sm[num] += 1
        print(sm)
        print(sorted(sm.items(), key=lambda item: item[1]))
        sm_list = sorted(sm.items(), key=lambda item: item[1])
        return [x[0] for x in sm_list[-k:]]


if __name__ == '__main__':
    slt = Solution()
    nums = [3, 0, 1, 0]
    k = 1
    print(slt.topKFrequent(nums, k))
