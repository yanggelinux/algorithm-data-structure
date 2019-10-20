# -*- coding: utf8 -*-



"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match_flag = False
        # 括号对应map
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        for k in s:
            # 如果字符是左括号，入栈
            if k in ["(", "[", "{"]:
                stack.append(k)
                # 匹配标示为True
                match_flag = True
            # 如果字符是右括号，出栈，并对比括号是否匹配
            if k in [")", "]", "}"]:
                if len(stack) > 0:
                    p = stack.pop()
                    # 括号不匹配返回False
                    if bracket_map[p] != k:
                        return False
                    else:
                        # 括号匹配匹配标示为重置False
                        match_flag = False
                else:
                    match_flag = True
        else:
            # 如果字符串都遍历完，还有每匹配的括号，返回False
            if match_flag or len(stack) > 0:
                return False
        return True

    def is_valid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) % 2 != 0:
            return False
        stack = ["?"]
        # 括号对应map
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        for k in s:
            if k in bracket_map:stack.append(k)
            if k in bracket_map.values():
                p = stack.pop()
                if k != bracket_map.get(p):return False
        else:
            if len(stack) >1:return False
        return True





if __name__ == '__main__':
    s = "()"
    slt = Solution()
    print(slt.is_valid2(s))
