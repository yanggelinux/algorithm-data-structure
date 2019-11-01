# -*- coding: utf8 -*-


"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:return 0
        low,high = 0,num
        while low <= high:
            mid = low + (high-low) // 2
            if mid * mid == num:return True
            elif mid*mid > num:
                high = mid -1
            else:
                low = mid +1
        return False

if __name__ == '__main__':
    slt = Solution()
    num = 16
    print(slt.isPerfectSquare(num))