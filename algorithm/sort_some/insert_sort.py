# -*- coding: utf8 -*-


# 插入排序

def insert_sort(arr):
    """
    插入排序，时间复杂度O(n^2)，空间复杂度O(1)，稳定排序算法
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(1, length):
        j = i - 1
        value = arr[i]
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
    return arr


def insert_sort2(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3]
    print(insert_sort2(arr))
