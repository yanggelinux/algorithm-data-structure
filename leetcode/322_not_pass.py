# -*- coding: utf8 -*-

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        res = 0
        coins = sorted(coins)
        coins.reverse()
        n = len(coins)
        for i in range(n):
            for j in range(n):
                if coins[j] <= amount:
                    print(111,coins[i],amount)
                    y = amount % coins[i]
                    count = amount // coins[i]
                    res += count
                    amount = y
                print(res)
        if res >0 and amount == 0:return res
        else:return -1





if __name__ == '__main__':
    slt = Solution()
    coins = [186,419,83,408]
    amount = 6249
    print(slt.coinChange(coins,amount))