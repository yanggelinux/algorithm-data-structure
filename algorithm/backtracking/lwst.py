# -*- coding: utf8 -*-


"""
回溯方式求字符串的莱文斯坦距离
"""


class Solution(object):

    def __init__(self):
        self.min_dist = 999999
        self.a = [s for s in "mitcmu"]
        self.b = [s for s in "mtacnu"]
        self.n = 6
        self.m = 6

    def lwst(self, i, j, edits):
        """
        回溯方式
        :param i:
        :param j:
        :param edits:
        :return:
        """
        if i == self.n or j == self.m:
            if i < self.n:
                edits += (self.n - i)
            if j < self.m:
                edits += (self.m - j)
            if edits < self.min_dist:
                self.min_dist = edits
            return
        if self.a[i] == self.b[j]:  # 两个字符串匹配
            self.lwst(i + 1, j + 1, edits)
        else:
            self.lwst(i + 1, j, edits + 1)  # 删除a[i]或者b[j]前面添加一个字符
            self.lwst(i, j + 1, edits + 1)  # 删除b[j]或者a[i]前面添加一个字符
            self.lwst(i + 1, j + 1, edits + 1)  # 将a[i]和b[i]替换成相同的字符


if __name__ == '__main__':
    slt = Solution()
    slt.lwst(0, 0, 0)
    print(slt.min_dist)
