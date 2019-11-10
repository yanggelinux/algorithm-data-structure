# -*- coding: utf8 -*-


"""
求最长公共子串
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

    def lcs(self, a, b, n, m):
        """
        求最长公共子串长度
        :param a:
        :param b:
        :param n:
        :param m:
        :return:
        """
        max_lcs = []
        for i in range(n):
            max_lcs.append([])
            for j in range(m):
                max_lcs[i].append(0)
        # 初始化第0行：a[0..0]与b[0..j]的maxlcs
        for j in range(m):
            if a[0] == b[j]:
                max_lcs[0][j] = 1
            elif j != 0:
                max_lcs[0][j] = max_lcs[0][j - 1]
            else:
                max_lcs[0][j] = 0
        # 初始化第0列：a[0..i]与b[0..0]的maxlcs
        for i in range(n):
            if a[i] == b[0]:
                max_lcs[i][0] = 1
            elif i != 0:
                max_lcs[i][0] = max_lcs[i - 1][0]
            else:
                max_lcs[i][0] = 0
        for i in range(1,n):
            for j in range(1,m):
                if a[i] == b[j]:
                    max_lcs[i][j] = max(max_lcs[i - 1][j - 1] + 1, max_lcs[i - 1][j], max_lcs[i][j - 1])
                else:
                    max_lcs[i][j] = max(max_lcs[i - 1][j - 1], max_lcs[i - 1][j], max_lcs[i][j - 1])
        self.print_matrix(max_lcs)
        return max_lcs[n-1][m-1]


if __name__ == '__main__':
    slt = Solution()
    a = [s for s in "mitcmu"]
    b = [s for s in "mtacnu"]
    n = len(a)
    m = len(b)
    print(slt.lcs(a, b, n, m))
