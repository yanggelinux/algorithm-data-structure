# -*- coding: utf8 -*-


"""

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dt = {}
        for idx,num in enumerate(nums):
            if dt.get(num) is not None:
                print(idx,dt[num])
                if idx - dt[num] <= k:
                    return True
                else:
                    dt[num] = idx
            else:
                dt[num] = idx
        return False



if __name__ == '__main__':
    slt = Solution()
    nums = [99,99]
    k = 2
    print(slt.containsNearbyDuplicate(nums,k))

