# -*- coding: utf8 -*-

"""
动态规划莱文斯坦距离实现
"""


class Solution(object):

    def print_matrix(self, matrix):
        """
        打印二维矩阵
        :param matrix:
        :return:
        """
        for mtx in matrix:
            print(mtx)

    def lwst(self, a, b, n, m):
        """
        动态规划求莱文斯坦距离
        :param a:
        :param b:
        :param n:
        :param m:
        :return:
        """
        min_dist = []
        for i in range(n):
            min_dist.append([])
            for j in range(m):
                min_dist[i].append(0)
        # 初始化第0行:a[0..0]与b[0..j]的编辑距离
        for j in range(m):
            if a[0] == b[j]:
                min_dist[0][j] = j
            elif j != 0:
                min_dist[0][j] = min_dist[0][j - 1] + 1
            else:
                min_dist[0][j] = 1
        for i in range(n):
            if a[i] == b[0]:
                min_dist[i][0] = i
            elif i != 0:
                min_dist[i][0] = min_dist[i - 1][0] + 1
            else:
                min_dist[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if a[i] == b[j]:
                    min_dist[i][j] = min(min_dist[i - 1][j] + 1, min_dist[i][j - 1] + 1, min_dist[i - 1][j - 1])
                else:
                    min_dist[i][j] = min(min_dist[i - 1][j] + 1, min_dist[i][j - 1] + 1, min_dist[i - 1][j - 1] + 1)
        self.print_matrix(min_dist)
        return min_dist[n-1][m-1]


if __name__ == '__main__':
    slt = Solution()
    a = [s for s in "mitcmu"]
    b = [s for s in "mtacnu"]
    n = len(a)
    m = len(b)
    print(slt.lwst(a, b, n, m))
