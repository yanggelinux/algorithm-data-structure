# -*- coding: utf8 -*-


"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

"""
def _min(heights):
    import sys
    min_h = sys.maxsize
    print(min_h)
    for h in heights:
        if h >0 and h < min_h:
            min_h = h
    return min_h


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        import sys
        max_area = 0
        n = len(heights)
        if n == 1:
            max_area = heights[0]
        for i in range(n):
            min_height = sys.maxsize
            for j in range(i,n):
                min_height = min(heights[j], min_height)
                x = (j - i) + 1
                area = x * min_height
                max_area = max(max_area, area)
        print(max_area)
        return max_area

    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while (stack[-1] != -1 and heights[stack[-1]] >= heights[i]):
                x = i - stack[-1] -1
                area = heights[stack.pop()] * x
                max_area = max(max_area,area)
            stack.append(i)
        while stack[-1] != -1:
            x = len(heights) - stack[-1] -1
            area = heights[stack.pop()] * x
            max_area = max(max_area, area)
        print(max_area)
        return max_area

    def largestRectangleArea3(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        heights = [0] + heights + [0]
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                max_area = max(max_area, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        print(max_area)
        return max_area








if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    # heights = [1,1,2,1]
    heights = [0,9]
    # heights = [0,9,0,8,8,0,2,2,0]
    slt = Solution()
    slt.largestRectangleArea3(heights)
