# -*- coding: utf8 -*-


class Solution(object):

    def __init__(self):
        self.res_list = []
        self.max_weight = -1

    def backtrack(self, start, nums):
        """
        回溯
        :param start:
        :return:
        """
        n = len(nums)
        if start == n:
            if nums not in self.res_list:
                self.res_list.append(nums[:])
        for i in range(start, n):
            # 调换位置
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(start + 1, nums)
            # 恢复状态
            nums[start], nums[i] = nums[i], nums[start]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        self.backtrack(start, nums)
        return self.res_list

    def pack(self, current_w, package_w, items, n, i):
        """

        :param current_w: 当前背包重量
        :param package_w: 背包最大能装的重量
        :param items: 物品的重量
        :param n: 物品的个数
        :param i: 考察到哪个物品了
        :return:
        """
        if current_w == package_w or i == n:  # current_w==package_w表示装满了;i==n表示已经考察完所有的物品
            if current_w > self.max_weight:
                self.max_weight = current_w
                print(self.max_weight)
            return
        self.pack(current_w, package_w, items, n, i + 1)  # 第i+1个物品选择不装进背包
        if current_w + items[i] <= package_w:
            self.pack(current_w + items[i], package_w, items, n, i + 1)  # 第i+1个物品选择装进背包

    def get_max(self):
        return self.max_weight


if __name__ == '__main__':
    slt = Solution()
    # nums = [1, 2, 3]
    # print(slt.permute(nums))
    items = [10, 20, 30, 40, 50]
    package_w = 100
    current_w = 0
    n = len(items)
    i = 0
    print(slt.pack(current_w, package_w, items, n, i))
    print(slt.get_max())
