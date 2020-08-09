# -*- coding: utf8 -*-


"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        暴力 超时
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        max_res = ""
        for i in range(n):
            for j in range(i, n):
                sp = s[i:j + 1]
                if sp == sp[::-1]:
                    if len(sp) > len(max_res): max_res = sp
        return max_res

    def longestPalindrome2(self, s):
        """
        优化
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        max_res = ""
        for i in range(n):
            j, k = i - 1, i + 1
            res = s[i]
            if s[i] == s[j] and j >= 1:
                res = s[j] + res
                if j > 1: j -= 1
            if k < n:
                if s[i] == s[k]:
                    res = res + s[k]
                    # k += 1
            print(i, j, k, res)
            while j >= 0 and k < n:
                if s[k] != s[j]: break
                if s[k] == s[j]:
                    res = s[j] + res
                    res = res + s[k]
                j -= 1
                k += 1
            print("res:",res)
            if len(res) > len(max_res): max_res = res
        return max_res


if __name__ == '__main__':
    slt = Solution()
    s = "aaaa"
    print(slt.longestPalindrome2(s))
