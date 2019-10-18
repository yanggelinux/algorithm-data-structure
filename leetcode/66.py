# -*- coding: utf8 -*-


"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

解题思路：分为三种情况
1、[6,6] 结果 [6,7]
2、[6,9] 结果 [7,0]
3、[9,9] 结果 [1,0,0]
从后往前遍历数组，每个元素依次加1，并对10取余，取余后的元素如果不等于0，直接返回数组，
循环结束后还没有返回，则说明是第三种情况，直接在数组前面插入1
"""

class Solution(object):
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_strs = [str(d) for d in digits]
        num_str = ''.join(digits_strs)
        num = int(num_str)
        num += 1
        num_str = str(num)
        i = 0
        print(num_str)
        for ns in num_str:
            digits[i] = int(ns)
            i += 1
        print(digits)

    def plus_one2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >=0:
            digits[i] += 1
            digits[i] %=10
            if digits[i] !=0:
                return digits
            i -= 1
        return [1] + digits



if __name__ == '__main__':
    slt = Solution()
    digits = [9,9]
    print(slt.plus_one2(digits))