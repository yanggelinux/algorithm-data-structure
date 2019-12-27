# -*- coding: utf8 -*-


"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
"""

from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        k = len(p)
        res_list = []
        if n < k: return res_list
        pm = {}
        for x in p:
            pm[x] = pm.get(x, 0) + 1
        for i in range(n - k + 1):
            j = i
            sm = {}
            step = 0
            while step < k:
                sm[s[j]] = sm.get(s[j], 0) + 1
                j += 1
                step += 1
                if sm == pm:
                    res_list.append(i)
        return res_list

    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        window = len(p)
        p_map = self.map(p)
        s_map = self.map(s[:window])
        for i in range(len(s) - window):
            if i > 0:
                left, right = ord(s[i - 1]) - ord("a"), ord(s[i + window - 1]) - ord("a")
                s_map[left] -= 1
                s_map[right] += 1
            if s_map == p_map: res.append(i)
        return res

    def map(self, st):
        m = [0] * 26
        for c in st:
            m[ord(c) - ord("a")] += 1
        return m


if __name__ == '__main__':
    slt = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(slt.findAnagrams2(s, p))
