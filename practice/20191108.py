# -*- coding: utf8 -*-


def print_states(states):
    """
    打印出states
    :param states:
    :return:
    """
    for state in states:
        print(state)


class Solution(object):

    def __init__(self):
        self.max_w = -1
        self.max_v = -1
        self.mem = []
        # n=5,w =9
        for i in range(5):
            self.mem.append([])
            for j in range(9 + 1):
                self.mem[i].append(False)

    def knapsack_backtrack(self, cw, i, weights, n, w):
        """
        0-1背包回溯算法，时间复杂度O(2^n)
        :param cw:
        :param i:
        :param weights:
        :param n:
        :param w:
        :return:
        """
        if cw == w or i == n:  # cw==w表示装满了，i==n表示物品都考察完了
            if cw > self.max_w:
                self.max_w = cw
            return
        self.knapsack_backtrack(cw, i + 1, weights, n, w)  # 不将第i个物品放入背包
        if cw + weights[i] <= w:  # 利用剪枝
            self.knapsack_backtrack(cw + weights[i], i + 1, weights, n, w)  # 将第i个物品放入背包

    def knapsack_backtrack2(self, cw, i, weights, n, w):
        """
        0-1背包回溯算法，时间复杂度O(2^n)
        :param cw:
        :param i:
        :param weights:
        :param n:
        :param w:
        :return:
        """
        if cw == w or i == n:  # cw==w表示装满了，i==n表示物品都考察完了
            if cw > self.max_w:
                self.max_w = cw
            return
        if self.mem[i][cw]: return
        self.mem[i][cw] = True
        self.knapsack_backtrack(cw, i + 1, weights, n, w)  # 不将第i个物品放入背包
        if cw + weights[i] <= w:  # 利用剪枝
            self.knapsack_backtrack(cw + weights[i], i + 1, weights, n, w)  # 将第i个物品放入背包

    def knapsack(self, weights, n, w):
        """
        0-1背包动态规划，时间复杂度O(n*w),空间复杂度(n*(w+1))
        :param weights:
        :param n:
        :param w:
        :return:
        """
        states = []
        for i in range(n):
            states.append([])
            for j in range(w + 1):
                states[i].append(False)
        # 第一行的数据做特殊处理，可以利用哨兵优化
        states[0][0] = True
        if weights[0] < w:
            states[0][weights[0]] = True
        # 从第二行开始，动态规划状态转移
        for i in range(1, n):
            for j in range(w + 1):  # 不把第i个物品放入背包
                if states[i - 1][j] == True:
                    states[i][j] = states[i - 1][j]
            for j in range(w - weights[i] + 1):  # 把第i个物品放入背包
                if states[i - 1][j] == True:
                    states[i][j + weights[i]] = True
        print_states(states)
        for i in range(w, -1, -1):  # 输出结果
            # 在最后一层，找到一个值为True的最接近w的值，就是背包中物品总重量的最大值
            if states[n - 1][i] == True:
                return i
        return 0

    def knapsack2(self, weights, n, w):
        """
        0-1背包动态规划优化版，时间复杂度O(n*w),空间复杂度O(w+1)
        :param weights:
        :param n:
        :param w:
        :return:
        """
        # 第一行的数据做特殊处理，可以利用哨兵优化
        states = [False] * (w + 1)
        if weights[0] <= w:
            states[weights[0]] = True
        # 从第二行开始，动态规划状态转移
        for i in range(1, n):
            for j in range(w - weights[i], -1, -1):  # 把第i个物品放入背包
                if states[j] == True:
                    states[j + weights[i]] = True
        # 输出结果
        for i in range(w, -1, -1):
            if states[i] == True:
                return i
        return 0

    def knapsack_backtrack3(self, cw, cv, i, weights, values, w, n):
        """
        0-1背包升级版，对于一组不同重量、不同价值、不可分割的物品
        我们选择将某些物品装入背包，在满足背包最大重量限制的前提下，背包中
        可装入物品的最大总价值
        回溯算法
        :param cw:当前物品总重量
        :param cv:当前物品总价值
        :param i:当前考察到第几个物品
        :param weights:重量列表
        :param values:价值列表
        :param w:背包最大承载重量
        :param n:物品个数
        :return:
        """
        if cw == w or i == n:
            if cv > self.max_v:
                self.max_v = cv
            return
        self.knapsack_backtrack3(cw, cv, i + 1, weights, values, w, n)  # 选择不装第i个物品
        if cw + weights[i] <= w:
            self.knapsack_backtrack3(cw + weights[i], cv + values[i], i + 1, weights, values, w, n)  # 选择装第i个物品

    def knapsack3(self, weights, values, n, w):
        """
        0-1背包升级版,动态规划
        :param weights:
        :param values:
        :param n:
        :param w:
        :return:
        """
        states = []
        # 初始化states
        for i in range(n):
            states.append([])
            for j in range(w + 1):
                states[i].append(-1)
        print_states(states)
        # 处理第一行
        states[0][0] = 0
        if weights[0] <= w:
            states[0][weights[0]] = values[0]
        # 从states第二行开始
        for i in range(1, n):
            for j in range(w + 1):
                if states[i - 1][j] >= 0:
                    states[i][j] = states[i - 1][j]
            for j in range(w - weights[i] + 1):
                if states[i - 1][j] >= 0:
                    v = states[i - 1][j] + values[i]
                    if v > states[i][j + weights[i]]:
                        states[i][j + weights[i]] = v
        max_v = -1
        for j in range(w + 1):
            if states[n - 1][j] > max_v:
                max_v = states[n - 1][j]
        return max_v


if __name__ == '__main__':
    slt = Solution()
    weights = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    n = 5
    w = 9
    # res = slt.knapsack2(weights, n, w)
    # print(res)
    # slt.knapsack_backtrack2(0, 0, weights, n, w)
    # print(slt.max_w)
    # slt.knapsack_backtrack3(0, 0, 0, weights, values, w, n)
    # print(slt.max_v)
    res = slt.knapsack3(weights, values, n, w)
    print(res)
