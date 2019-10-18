# -*- coding: utf8 -*-

"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""

def partition(arr,low,high):
    """
    数据分隔算法
    :param arr:
    :param low:
    :param high:
    :return:
    """
    #选取最右边的元素当作分隔点
    pivot = arr[low]
    while low < high:
        #从右往左走，high -1
        while low < high and arr[high] >= pivot:
            high -= 1
        #如果遇到比pivot小的数据，交换位置,小于pivot的数据，移动到左边
        arr[low] = arr[high]
        #从右往左走,low + 1
        while low < high and arr[low] <= pivot:
            low += 1
        #遇到比pivot大的数据，互换位置，大于pivot的数据移动到右边
        arr[high] = arr[low]
    #当两点相遇的时候low=high
    arr[low] = pivot
    return low

def quick_sort(arr,low,high):
    """

    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
    return arr
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        时间复杂度O(m+n),空间复杂度O(m+n)
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res = []
        i = 0
        j = 0
        while 1:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i +=1
                else:
                    res.append(nums2[j])
                    j += 1
            elif i < m and j >= n:
                res.append(nums1[i])
                i += 1
            elif i>=m and j < n:
                res.append(nums2[j])
                j += 1
            else:break
        print(res)

    def merge2(self, nums1, m, nums2, n):
        """
        时间复杂度O(m+nlogm+n),空间复杂度O(m+n)
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        quick_sort(nums1,0,len(nums1)-1)
        print(nums1)

    def merge3(self, nums1, m, nums2, n):
        """
        时间复杂度O(m+n),空间复杂度O(m+n)
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #拷贝一个新的list
        num1_copy = nums1[:]
        i = 0
        j = 0
        k = 0
        while 1:
            if i < m and j < n:
                if num1_copy[i] <= nums2[j]:
                    nums1[k]=num1_copy[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            elif i < m and j >= n:
                nums1[k]=num1_copy[i]
                i += 1
            elif i >= m and j < n:
                nums1[k] = nums2[j]
                j += 1
            else:break
            k += 1
        print(nums1)

    def merge4(self, nums1, m, nums2, n):
        """
        时间复杂度O(m+n),空间复杂度O(1)
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 拷贝一个新的list
        i = m -1
        j = n -1
        k = m + n - 1
        while k >= 0:
            if i >= 0 and j >= 0 :
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i-=1
                else:
                    nums1[k] = nums2[j]
                    j-=1
            elif i >= 0 and j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif i < 0 and j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            else:
                break
            k -= 1
        print(nums1)


if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    slt = Solution()
    slt.merge4(nums1, m, nums2, n)
