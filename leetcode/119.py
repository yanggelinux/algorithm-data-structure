# -*- coding: utf8 -*-

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res_list = []
        for i in range(1, rowIndex + 2):
            base = [1] * i
            if i <= 2:
                res_list.append(base)
            else:
                for j in range(i - 1):
                    if j > 0 and j < i:
                        base[j] = res_list[i - 2][j - 1] + res_list[i - 2][j]
                res_list.append(base)
        return res_list[-1]

if __name__ == '__main__':
    slt = Solution()
    rowIndex = 3
    print(slt.getRow(rowIndex))
