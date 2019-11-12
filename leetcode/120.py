# -*- coding: utf8 -*-

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

动态规划状态转移方程opt[i,j] = min(opt[i-1][j],opt[i-1][j-1]) + opt[i,j]
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return
        states = [[0 for i in range(len(row))] for row in triangle]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    states[i][j] = states[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    states[i][j] = states[i - 1][j - 1] + triangle[i][j]
                else:
                    states[i][j] = min(states[i - 1][j - 1], states[i - 1][j]) + triangle[i][j]
        for state in states:
            print(state)
        return min(states[-1]) + triangle[0][0]


if __name__ == '__main__':
    slt = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]
    slt.minimumTotal(triangle)