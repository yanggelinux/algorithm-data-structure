# -*- coding: utf8 -*-



"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):

    def __init__(self):
        self.res_list = []

    def _generate(self,left,right,n,s):
        """

        :param left:
        :param right:
        :param n:
        :param s:
        :return:
        """
        if left == n and right == n:
            self.res_list.append(s)
            return
        if left < n:
            self._generate(left+1,right,n,s+"(")
        if right < left:
            self._generate(left,right+1,n,s+")")


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left,right,s = 0,0,""
        self._generate(left,right,n,s)
        return self.res_list


if __name__ == '__main__':
    slt = Solution()
    print(slt.generateParenthesis(3))