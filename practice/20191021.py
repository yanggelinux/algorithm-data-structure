# -*- coding: utf8 -*-




class Solution(object):

    def is_vaild(self,strs):
        """
        leetcode 20
        :param strs:
        :return:
        """
        map = {"(": ")", "[": "]", "{": "}"}
        left_list = ["(", "[", "{"]
        right_list = [")", "]", "}"]
        stack = []
        for s in strs:
            if s in left_list:
                stack.append(s)
            elif s in right_list:
                if len(stack) > 0:
                    b = stack.pop()
                    if map.get(b) != s: return False
                else:
                    return False
        if len(stack) > 0: return False
        return True


    def remove_duplicates(self, nums):
        """
        leetcode 26
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
        return j+1

    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        for i in range(n,-1,-1):
            digits[i] += 1
            digits[i] %=10
            if digits[i] != 0:
                return digits
        digits = [1] + digits
        return digits
    def plus_one2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dd = int(''.join([str(d) for d in digits])) + 1
        return [int(d) for d in list(str(dd))]

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        return nums1.sort()

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:]
        l = m + n -1
        i = 0
        j = 0
        k = 0
        while k <= l:
            if i < m and j <n:
                if nums1_copy[i] <= nums2[j]:
                    nums1[k] = nums1_copy[i]
                    i+=1
                else:
                    nums1[k] = nums2[j]
                    j+=1
            elif i < m and j >=n:
                nums1[k] = nums1_copy[i]
                i+=1
            elif i >=m and j < n:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        return nums1

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        map = {}
        for i in range(n):
            a = nums[i]
            b = target - a
            if b in map and map.get(b) != i:
                return [map.get(b), i]
            map[a] = i


if __name__ == '__main__':
    slt = Solution()
    # strs = "()[]{}]"
    # print(slt.is_vaild(strs))
    # nums = [0,0,1,1,1,2,2,3,3,4]
    # slt.remove_duplicates(nums)
    # digits= [4,3,2,1]
    # slt.plus_one2(digits)
    # nums1 = [4, 5, 6, 0, 0, 0]
    # m = 3
    # nums2 = [1, 2, 3]
    # n = 3
    # print(slt.merge2(nums1,m,nums2,n))
    nums = [2, 7, 11, 15]
    target = 9
    print(slt.two_sum(nums, target))