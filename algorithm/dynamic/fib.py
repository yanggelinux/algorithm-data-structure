# -*- coding: utf8 -*-


"""
动态规划求解fib
"""


class Solution(object):

    def fib(self, n):
        """
        傻递归斐波拉切
        :param n:
        :return:
        """
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n, memo):
        """
        加缓存的斐波拉切
        :param n:
        :param memo:
        :return:
        """
        if n <= 1:
            return n
        if memo[n] == 0:
            memo[n] = self.fib2(n - 1, memo) + self.fib2(n - 2, memo)
            print(memo)
        return memo[n]

    def fib3(self, n):
        """
        迭代法
        :param n:
        :return:
        """
        res = []
        i, a, b = 0, 0, 1
        while i < n:
            res.append(a)
            a, b = b, a + b
            i += 1
        print(res)
        return a


if __name__ == '__main__':
    slt = Solution()
    print(slt.fib(6))
    # print(slt.fib2(6,[0]*7))
    print(slt.fib3(6))
