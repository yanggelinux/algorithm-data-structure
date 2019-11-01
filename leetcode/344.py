# -*- coding: utf8 -*-


"""

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

"""


class Solution(object):
    def reverseString(self, s):
        """
        迭代的方式
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n -1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i +=1
            j-=1
        return s

    def reverseString2(self, s):
        """
        递归的方式
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        def helper(i,j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            helper(i,j)

        n = len(s)
        i = 0
        j = n - 1
        helper(i,j)
        return s

if __name__ == '__main__':
    slt = Solution()
    s = ["H","a","n","n","a","h"]
    print(slt.reverseString2(s))