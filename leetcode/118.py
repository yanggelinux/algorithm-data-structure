# -*- coding: utf8 -*-

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res_list = []
        for i in range(1,numRows+1):
            base = [1] * i
            if i <= 2:
                res_list.append(base)
            else:
                for j in range(i-1):
                    if j > 0 and j < i:
                        base[j] = res_list[i-2][j-1] + res_list[i-2][j]
                res_list.append(base)
        return res_list



if __name__ == '__main__':
    slt = Solution()
    numRows = 5
    print(slt.generate(numRows))