# -*- coding: utf8 -*-


"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return n > 0 and n & (n - 1) == 0
        if n <= 0:return False
        if n == 1:return True
        while 1:
            n = n / 2
            if n == 1.0:
                return True
            if n < 1.0:break
        return False


if __name__ == '__main__':
    slt = Solution()
    n = 3
    print(slt.isPowerOfTwo(n))
