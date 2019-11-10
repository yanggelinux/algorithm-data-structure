# -*- coding: utf8 -*-


"""
﻿假设我们有一个n乘以n的矩阵w[n][n]。矩阵存储的都是正整数。棋子起始的位置在左上角，终止的位置在右下角。我们将棋子从左上角移动到右下角。
每次只能向右或者向下移动一位从左上角到右下角，会有很多不同的路径可以走。我们把每条路径经过的数字加起来看作路径的长度。
那么从左上移动到右下角的最短路径长度是多少呢？
[ [1，3，5，9],
  [2，1，3，4]，
  [5，2，6，7]，
  [6，8，4，3] ]
"""


class Solution(object):

    def __init__(self):
        self.min_dist = 99999

    def get_min_dist(self, i, j, dist, w, n):
        """
        回溯法，获取最短路径最后一步
        :param i: 行
        :param j: 列
        :param dist:当前路径
        :param w: 二维矩阵
        :param n: 二维矩阵的长宽减1
        :return:
        """
        if i == n-1 and j == n-1: #到达了n-1, n-1这个位置了
            if dist < self.min_dist:
                self.min_dist = dist
            return
        if (i < n-1):  # 往下走 更新i=i+1, j=j
            self.get_min_dist(i + 1, j, dist + w[i][j], w, n)
        if (j < n-1):  # 往右走，更新i=i, j=j+1
            self.get_min_dist(i, j + 1, dist + w[i][j], w, n)
    def min_dist_backtrack(self,w,n):
        """
        获取最短路径
        :param w:
        :param n:
        :return:
        """
        return self.min_dist + w[n-1][n-1]

if __name__ == '__main__':
    slt = Solution()
    w = [[1,3,5,9],[2,1,3,4],[5,2,6,7],[6,8,4,3]]
    slt.get_min_dist(0,0,0,w,4)
    print(slt.min_dist_backtrack(w,4))
