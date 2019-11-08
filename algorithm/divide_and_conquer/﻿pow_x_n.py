# -*- coding: utf8 -*-


"""
﻿实现 pow(x, n) ，即计算 x 的 n 次幂函数
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        return self.divide(x,n)
    def divide(self,x,n):
        """
        分治
        :param x:
        :param n:
        :return:
        """
        if n == 1:return x
        if n == 0:return 1
        sub_res = self.divide(x,n//2)
        if n % 2 == 1:
            return sub_res * sub_res * x
        else:
            return sub_res * sub_res