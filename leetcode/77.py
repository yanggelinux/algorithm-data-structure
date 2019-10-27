# -*- coding: utf8 -*-


"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        if n < 0 or k < 0 or n < k:
            return results
        def backtrack(start,res):
            #递归终止条件
            if len(res) == k:
                results.append(res[:])
                return
            for i in range(start,n+1):
                res.append(i)
                backtrack(i+1,res)
                #回溯时状态重置
                res.pop()
        backtrack(start=1,res=[])
        return results




if __name__ == '__main__':
    slt = Solution()
    print(slt.combine(4,2))