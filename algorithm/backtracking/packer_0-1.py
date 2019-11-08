# -*- coding: utf8 -*-

"""
我们有一个背包，背包的承载重量是Wkg。
现在我们有n个物品，每个物品的重量不等，并且不可分割。
我们现在期望选择几件物品，装到背包中。
在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大
"""
class Solution(object):

    def __init__(self):
        self.max_weight = -1

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


if __name__ == '__main__':
    slt = Solution()
    items = [10, 20, 30, 40, 50]
    package_w = 100
    current_w = 0
    n = len(items)
    i = 0
    slt.pack(current_w, package_w, items, n, i)