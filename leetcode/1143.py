# -*- coding: utf8 -*-

"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

 

示例 1:

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
 

提示:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。

思路：

﻿我们从a[0]和b[0]开始，以此考察两个字符串中的字符是否匹配。
1）如果a[i]与b[j]相互匹配，我们把最大公共子串长度加1，并且继续考察a[i+1] 和b[j+1]。
2）如果a[i]与b[j]不相互匹配，最长公共子串长度不变，这个时候有两个不同的决策路线：
2-1）删除a[i]，或者在b[j]前面加上一个字符a[i]，然后继续考察考察a[i+1] 和b[j]。
2-2）删除b[j]，或者在a[i]前面加上一个字符b[j]，然后继续考察考察a[i] 和b[j+1]。
a[0...i]和b[0...j]的最长公共子串长度max_lcs(i,j)，只有可能从下面三个状态转移过来：
1）(i-1,j-1,max_lcs)，其中max_lcs表示a[0...i-1]和b[0...j-1]的最长公共子串长度。
2）(i-1,j,max_lcs)，其中max_lcs表示a[0...i-1]和b[0...j]的最长公共子串长度。
3）(i,j-1,max_lcs)，其中max_lcs表示a[0...i]和b[0...j-1]的最长公共子串长度。
状态转移方程
如果：a[i]==b[j]，那么：max_lcs(i, j)就等于：
max(max_lcs(i-1,j-1)+1, max_lcs(i-1, j), max_lcs(i, j-1))；
简化：max_lcs(i-1,j-1)+1；
如果：a[i]!=b[j]，那么：max_lcs(i, j)就等于：
max(max_lcs(i-1,j-1), max_lcs(i-1, j), max_lcs(i, j-1))；
简化： max(max_lcs(i-1, j), max_lcs(i, j-1))
其中max表示求三数中的最大值。

"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        n = len(text1)
        m = len(text2)
        states = []
        for i in range(n):
            states.append([])
            for j in range(m):
                states[i].append(0)
        #初始化状态转移表第一行
        for j in range(m):
            if text1[0] == text2[j]:
                states[0][j] = 1
            elif j != 0:
                states[0][j] = states[0][j-1]
            else:
                states[0][j] = 0
        # 初始化状态转移表第一列
        for i in range(n):
            if text1[i] == text2[0]:
                states[i][0] = 1
            elif i !=0 :
                states[i][0] = states[i-1][0]
            else:
                states[i][0] = 0
        #填状态转移表
        for i in range(1,n):
            for j in range(1,m):
                if text1[i] == text2[j]:
                    states[i][j] = states[i-1][j-1] +1
                else:
                    states[i][j] = max(states[i-1][j],states[i][j-1])
        return states[n-1][m-1]


if __name__ == '__main__':
    slt = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(slt.longestCommonSubsequence(text1,text2))