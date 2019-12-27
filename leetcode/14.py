# -*- coding: utf8 -*-


"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:return ""
        base = strs[0]
        n = len(base)
        i = 0
        for i in range(n):
            for s in strs:
                if not s.startswith(base[:i+1]):
                    return base[:i]

        return base[:i+1]


if __name__ == '__main__':
    slt = Solution()
    strs = ["dog","racecar","car"]
    strs = ["a","a"]
    print(slt.longestCommonPrefix(strs))