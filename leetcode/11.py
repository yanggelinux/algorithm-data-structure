# -*- coding: utf8 -*-


"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

"""


class Solution(object):
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        print(max_area)
        return max_area

    def max_area2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            if height[i] < height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[j]
                j -= 1
            max_area = max(max_area, area)
        print(max_area)
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    slt = Solution()
    print(slt.max_area2(height))
