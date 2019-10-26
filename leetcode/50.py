# -*- coding: utf8 -*-



"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""
class Solution(object):
    def myPow(self, x, n):
        """
        暴力法时间复杂度O(n)
        :type x: float
        :type n: int
        :rtype: float
        """
        j = n
        if n < 0:
            j = -n
        res = float(1)
        for i in range(j):
            res = res * float(x)
        if n < 0:
            res = 1 / res
        return res

    def myPow2(self, x, n):
        """
        分治法时间复杂度O(logn)
        :type x: float
        :type n: int
        :rtype: float
        """
        x = float(x)
        if n < 0:
            x = float(1/x)
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
            sub_res = sub_res * sub_res * x
        else:
            sub_res = sub_res * sub_res
        return sub_res



if __name__ == '__main__':
    slt = Solution()
    print(slt.myPow(0.44528,0))