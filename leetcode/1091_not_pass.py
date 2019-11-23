# -*- coding: utf8 -*-


"""
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

 

示例 1：

输入：[[0,1],[1,0]]

输出：2

示例 2：

输入：[[0,0,0],[1,1,0],[1,1,0]]

输出：4

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 为 0 或 1

"""


def print_somes(somes):
    for some in somes:
        print(some)
    print("-" * 10)


class Solution(object):

    def _min(self,x,y,z,max_val):
        """
        获取符合条件的最小值
        :param x:
        :param y:
        :param z:
        :param max_val:
        :return:
        """
        min_val = min(x,y,z)
        if min_val >= max_val:
            return -2
        else:
            return min_val

    def shortestPathBinaryMatrix(self, grid):
        """
        动态规划，动态转移方程是
        if grid[i][j] == 0:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        else:
            dp[i][j] = 0
        :type grid: List[List[int]]
        :rtype: int
        """
        print_somes(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1 : return -1
        m = len(grid[0])
        n = len(grid)
        max_val = m * n
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(m):
                dp[i].append(0)
        # 初始化状态转移表第一行
        dp[0][0] = 1
        for j in range(1,m):
            if grid[0][j] == 0:
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = max_val
        # 初始化状态转移表第一列
        for i in range(1,n):
            if grid[i][0] == 0:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = max_val
        # 从第二行，第二列填状态转移表
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 0:
                    dp[i][j] = self._min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1],max_val) + 1
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = max_val
        print_somes(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    slt = Solution()
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,0,0]]
    grid = [[0,0,1,1,1],[1,0,1,1,1],[0,1,1,1,0],[0,0,1,1,1],[0,0,0,0,0]]
    print(slt.shortestPathBinaryMatrix(grid))
