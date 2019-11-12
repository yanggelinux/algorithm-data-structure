# -*- coding: utf8 -*-


"""
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

[
 [start,0,0,0,0,0,0]
 [0,0,0,0,0,0,0]
 [0,0,0,0,0,0,finsh]
                ]

例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
利用动态规划递推公式
opt[i,j] = opt[i-1,j] + opt[i,j-1]

"""

def print_somes(somes):
    for some in somes:
        print(some)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1: return m
        if n <= 1: return n
        states = []
        for i in range(n):
            states.append([])
            for j in range(m):
                states[i].append(0)
        #初始化第一行
        for j in range(1,m):
            states[0][j] = 1
        # 初始化第一列
        for i in range(1,n):
            states[i][0] = 1
        #开始填状态转移表
        for i in range(1,n):
            for j in range(1,m):
                states[i][j] = states[i-1][j] + states[i][j-1]
        return states[n-1][m-1]



if __name__ == '__main__':
    slt = Solution()
    m = 1
    n = 0
    print(slt.uniquePaths(m,n))