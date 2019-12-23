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
        # 若数组nums为空或长度小于3直接返回
        if not nums or n < 3:
            return res_list
        # 对数组进行排序
        nums.sort()
        for i in range(n):
            # 对于重复元素直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                # 左指针
                l = i + 1
                # 右指针
                r = n - 1
                while l < r:
                    # 当 nums[i] + nums[l] + nums[r] == 0 符合条件，左右指针移动
                    if nums[i] + nums[l] + nums[r] == 0:
                        res_list.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # 判断左界和右界和下一位是否有重复，如果有各移动一位
                        while l < n - 1 and nums[l] == nums[l - 1]:
                            l += 1
                        while r > 0 and nums[r] == nums[r + 1]:
                            r -= 1
                    # 若和小于0，说明nums[l]太小，l+1 右移
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    # 若和大于0，说明nums[r]太大，r-1左移
                    else:
                        r -= 1
        return res_list


if __name__ == '__main__':
    nums = [1, -1, -1, 0]
    slt = Solution()
    print(slt.three_sum2(nums))
