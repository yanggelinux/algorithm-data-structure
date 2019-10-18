# -*- coding: utf8 -*-


"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

解题思路：

利用快慢两个指针i，j，遍历整个数组，当遇到nums[i] != nums[j] 的时候 i=i+1 ,nums[i] 就等于 nums[j],
j=j+1，当j=n即遍历完整个数组的时候，位置移动完成
          nums                    i j
[0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4] 0 2
[0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4] 1 3
[0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4] 1 4
[0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4] 1 5
[0, 1, 2, 1, 1, 2, 2, 3, 3, 3, 4] 2 6
[0, 1, 2, 1, 1, 2, 2, 3, 3, 3, 4] 2 7
[0, 1, 2, 3, 1, 2, 2, 3, 3, 3, 4] 3 8
[0, 1, 2, 3, 1, 2, 2, 3, 3, 3, 4] 3 9
[0, 1, 2, 3, 1, 2, 2, 3, 3, 3, 4] 3 10
[0, 1, 2, 3, 4, 2, 2, 3, 3, 3, 4] 4 11
"""

class Solution(object):

    def remove_duplicates(self, nums):
        """
        直接改变删除列表中元素
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        i = 0
        j = 1
        while j <= n:
            if nums[i] == nums[j]:
                nums = nums[0:i] + nums[j:]
                n-=1
            else:
                i+=1
                j+=1
        print(nums)
        return len(nums)

    def removeDuplicates(self, nums):
        """
        不改变直接移动列表中元素
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) -1
        i = 0
        j = 1
        while j <= n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j+=1
        print(nums)
        return i+1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4]
    # nums = [1,1,2]
    s = Solution()
    print(s.removeDuplicates(nums))
