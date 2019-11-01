# -*- coding: utf8 -*-




class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        possible_words = list(set([w for w in ''.join(wordList)]))
        # possible_words = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        queue = [(beginWord,1)]
        visited = set()
        while queue:
            word,step = queue.pop(0)
            if word == endWord:
                return step
            for i in range(len(word)):
                for p in possible_words:
                    temp_word = word[:i] + p + word[i+1:]
                    if temp_word in wordList and temp_word not in visited:
                        queue.append((temp_word,step+1))
                        visited.add(temp_word)
        return 0

    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five,ten = 0,0
        for bill in bills:
            if bill == 5:
                five +=1
            elif bill == 10:
                if five == 0:return False
                five -=1
                ten +=1
            else:
                if five >=1 and ten >=1:
                    five -= 1
                    ten -= 1
                elif five >=3:
                    five -= 3
                else:
                    return False
        return True

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        n = len(g)
        k = len(s)
        i = 0
        j = 0
        while i < n and j < k:
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i

    def binary_search(self,nums,target):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right -left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None
    def find_roate_index(self,nums):
        """
        寻找选择数组的分割点
        :param nums:
        :return:
        """
        if not nums:return 0
        left,right = 0 , len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid -1]:
                return mid
            else:
                if nums[mid] < nums[right]:
                    right = mid -1
                else:
                    left = mid + 1
        return 0

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        pivot = self.find_roate_index(nums)
        numsa = nums[:pivot]
        numsb = nums[pivot:]
        resa = self.binary_search(numsa,target)
        resb = self.binary_search(numsb,target)
        if resa is not None:
            return resa
        if resb is not None:
            return pivot + resb
        if resa is None and resb is None:
            return -1











if __name__ == '__main__':
    slt = Solution()

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log"]
    # print(slt.ladderLength(beginWord,endWord,wordList))
    # g = [1, 2, 3]
    # s = [1, 1]
    # print(slt.findContentChildren(g,s))
    nums = [4, 5, 6, 7, 0, 1, 2]
    slt.search(nums,6)