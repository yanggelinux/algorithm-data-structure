# -*- coding: utf8 -*-

"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res_list = []
        visited = []
        wordList = set(wordList)  # list转换成set，提高执行时间，in操作时间复杂度O(1)
        possible = ''.join(list(wordList))
        possible_list = list(set([x for x in possible]))
        if endWord not in wordList:
            return res_list
        queue = [(beginWord, [beginWord])]
        while queue:
            print ('queue',queue)
            word, res = queue.pop(0)
            print('word-res',word,res)
            if word == endWord:
                res_list.append(res)
                # res = []
            for i in range(len(word)):
                for p in possible_list:
                    temp_word = word[:i] + p + word[i + 1:]
                    if temp_word in wordList and (temp_word not in visited):
                        queue.append((temp_word, res + [temp_word]))
                        visited.append(temp_word)
                        # wordList.remove(temp_word)
        return res_list


if __name__ == '__main__':
    slt = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(slt.findLadders(beginWord, endWord, wordList))