# -*- coding: utf8 -*-


"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        利用有序字典，python3.6以后字典是有序的
        :type s: str
        :rtype: int
        """
        s_map = {}
        s = [x for x in s]
        for x in s:
            if s_map.get(x) is None:
                s_map[x] = 0
            else:
                s_map[x] += 1
        idx = 0
        for k,v in s_map.items():
            if v == 0:
                return s.index(k)
            idx +=1
        return -1


if __name__ == '__main__':
    slt = Solution()
    s = "dddccdbba"
    print(slt.firstUniqChar(s))