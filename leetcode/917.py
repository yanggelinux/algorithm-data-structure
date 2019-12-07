# -*- coding: utf8 -*-

"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 

提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "

"""


class Solution(object):

    def is_word(self, s):
        """
        判断是否是字母
        :param s:
        :return:
        """
        return s.isalpha()

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list(S)
        n = len(s)
        i = 0
        j = n - 1
        while i <= j:
            if self.is_word(s[i]) is True and self.is_word(s[j]) is True:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif self.is_word(s[i]) is False and self.is_word(s[j]) is True:
                i += 1
            elif self.is_word(s[i]) is True and self.is_word(s[j]) is False:
                j -= 1
            else:
                i += 1
                j -= 1
        return "".join(s)


if __name__ == '__main__':
    slt = Solution()
    S = "Qedo1ct-eeLg=ntse-T!"
    slt.reverseOnlyLetters(S)
    slt.is_word("-")
