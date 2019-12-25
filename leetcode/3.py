# -*- coding: utf8 -*-


"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        暴力超时
        :type s: str
        :rtype: int
        """
        max_length = 0
        if not s: return 0
        for i in range(len(s)):
            st = set()
            res = 0
            for x in s[i:]:
                if x not in st:
                    res += 1
                else:
                    res = 0
                    st = set()
                    res += 1
                st.add(x)
                max_length = max(res, max_length)
        return max_length

    def lengthOfLongestSubstring2(self, s):
        """
        优化
        这道题主要用到思路是：滑动窗口
        什么是滑动窗口？
        其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
        如何移动？
        我们只要把队列的左边的元素移出就行了，直到满足题目要求！
        一直维持这样的队列，找出队列出现最长的长度时候，求出解！
        时间复杂度：O(n)
        :type s: str
        :rtype: int
        """
        if not s :return 0
        max_length = 0
        left_idx = 0
        cur_length = 0
        st = set()
        n = len(s)
        for i in range(n):
            cur_length += 1
            while s[i] in st:
                st.remove(s[left_idx])
                left_idx += 1
                cur_length -= 1
            st.add(s[i])
            max_length = max(cur_length,max_length)
        return max_length





if __name__ == '__main__':
    slt = Solution()
    s = "abcabcbb"
    print(slt.lengthOfLongestSubstring2(s))
