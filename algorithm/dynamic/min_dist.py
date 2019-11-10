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
        self.mem = []
        for i in range(4):
            self.mem.append([])
            for j in range(4):
                self.mem[i].append(0)

    def print_matrix(self, matrix):
        for mtx in matrix:
            print(mtx)

    def min_dist_dp(self, matrix, n):
        """
        动态规划状态转移表，求最小路径
        :param matrix: 路径二维矩阵
        :param n: 路径二维矩阵长宽
        :return:
        """
        # 初始化保存状态的二维矩阵
        states = []
        for i in range(n):
            states.append([])
            for j in range(n):
                states[i].append(0)
        # 初始化states的第一行
        sum = 0
        for j in range(n):
            sum += matrix[0][j]
            states[0][j] = sum
        # 初始化states的第一列
        sum = 0
        for i in range(n):
            sum += matrix[i][0]
            states[i][0] = sum
        for i in range(1, n):
            for j in range(1, n):
                states[i][j] = matrix[i][j] + min(states[i - 1][j], states[i][j - 1])
        self.print_matrix(states)
        return states[n - 1][n - 1]

    def min_dist_dp2(self, i, j, matrix, n):
        """
        动态规划状态转移方程 备忘录，求最小路径
        :param i:
        :param jmatrix:
        :param n:
        :return:
        """

        if i == 0 and j == 0:
            return matrix[0][0]
        if self.mem[i][j] > 0:
            return self.mem[i][j]
        min_left = 999999
        if j - 1 >= 0:
            min_left = self.min_dist_dp2(i, j - 1, matrix, n)
        min_up = 999999
        if i - 1 >= 0:
            min_up = self.min_dist_dp2(i - 1, j, matrix, n)
        cur_min_dist = matrix[i][j] + min(min_left, min_up)
        self.mem[i][j] = cur_min_dist
        return cur_min_dist


if __name__ == '__main__':
    slt = Solution()
    matrix = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    n = 4
    print(slt.min_dist_dp2(3, 3, matrix, n))
