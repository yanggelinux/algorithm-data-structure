# -*- coding: utf8 -*-

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

[
 [start,0,0,0,0,0,0]
 [0,0,0,1,0,0,0]
 [0,0,0,0,0,0,finsh]
                ]

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
if opt[i,j] == 0:
    opt[i,j] = opt[i-1,j] + opt[i,j-1]
else:
    opt[i,j] = 0

"""


def print_somes(somes):
    for some in somes:
        print(some)


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 初始化第一行
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        if m == 0:return m
        if n == 0:return n
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        #初始化第一行
        for j in range(1,m):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)
        # 初始化第一列
        for i in range(1,n):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        # 开始填状态转移表
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[n - 1][m - 1]


if __name__ == '__main__':
    slt = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(slt.uniquePathsWithObstacles(obstacleGrid))
