# -*- coding: utf8 -*-

#快速排序
#
# 算法思想
# 快速排序的核心思想在于：首先在这个序列中随便找一个数作为基准数，然后将这个序列中所有比基准数大的数放在该数字的右边，比基准数小的数放在该数字的左边。
# 第一轮排序结束之后，再分别对已经好的基准书左边（比基准数小）和基准书右边（比基准书大）的数字序列重复上述操作，用递归形式即可实现快速排序，完成对整个序列的排序。
#
# 算法步骤
# 为了清晰地展示快速排序的原理，这里使用一个例子来具体说明快速排序算法排序的过程。
# 假定现在要对数字序列 [4, 2, 7，8, 0，1, 5，23] 进行快速排序。
# 我们假设最左边的编号为i，最左边的编号为j，不失一般性，假定以4作为基准进行排序（每一次总总是让j先出发，向左移动，再让i出发，向右移动）。
#
# （一）第一轮排序
# [4, 2, 7，8, 0，1, 5，23]
# j向左出发寻找第一个小于4的数，遇到1的时候停下来；i向右出发寻找第一个大于4的数，遇到7的时候停下来，交换两者的位置，数字序列变为
# [4,2,1,8,0,7,5,23]
# 接下继续让j向左移动，寻找第二个小于4的数，遇到0的时候停下来；让i向右移动，寻找第二个大于4的数，遇到8的时候停下来，交换两者的位置，数字序列变为
# [4,2,1,0,8,7,5,23]
# 此时发现i与j相遇了，第一轮排序结束，调换4和0的位置，数字序列变为
# [0,2,1,4,8,7,5,23],
# 所有小于4的数字都在4的左边，所有大于4的数字都在4的右边。
#
# （二）第二轮排序
# 分别对4左边和4右边的数字序列进行排序处理，首先对4左边的数字序列[0,2,1]排序。
# 以第一个数字0为基准，j向左出发寻找第一个小于0的数，i向右出发寻找第一个大于0的数，遇到0的时候停下来，如果找到就交换两者的位置，否则不变。数字序列变为[0,2,1]，所有小于0的数字都在0的左边，所有大于0的数字都在0的右边。
# 再对4右边的数字序列[8, 7，5,23]排序。
# 以第一个数字8为基准，j向左出发寻找第一个小于8的数，遇到5的时候停下来；i向右出发寻找第一个大于8的数，如果找到就交换两者的位置，同时保证i小于j，那么数字序列变为[5,7,8,23]。所有小于8的数字都在8的左边，所有大于8的数字都在8的右边。
# 总体数字序列变为[0,2,1,4,5,7,8,23]。
#
# （三）第三轮排序
# 好了动手算一算，类似第一和第二轮的排序方法，对0右边的数字序列进行排序，得到[0,1,2]；对8左边的数字序列进行排序，得到[5,7，8，23]。第三轮排序结束。
# 得到最终的排序结果为
# [0,1,2,4,5,7,8,23]。
# 快排过程结束。


def fake_quick_sort(arr):
    """
    快速排序伪代码，时间复杂度O(nlogn)，空间复杂度O(n),不稳定排序算法
    效率较低
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less_arr = fake_quick_sort([i for i in arr[1:] if i <= pivot])
    large_arr = fake_quick_sort([i for i in arr[1:] if i > pivot])
    return less_arr + [pivot] + large_arr

def partition(arr,low,high):
    """
    找到最佳分隔点
    :param arr:
    :param low:
    :param high:
    :return:
    """
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1

def quick_sort(arr,low,high):
    """
    快速排序，时间复杂度O(nlogn)，空间复杂度O(1),不稳定排序算法
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        p = partition(arr,low,high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr

def partition2(arr,low,high):
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

def quick_sort2(arr,low,high):
    """

    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        p = partition2(arr,low,high)
        quick_sort2(arr,low,p-1)
        quick_sort2(arr,p+1,high)
    return arr



if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3,2]
    # arr = [1, 4, 2, 6, 5, 3, 2]
    # print(fake_quick_sort(arr))
    print(quick_sort2(arr,0,len(arr)-1))