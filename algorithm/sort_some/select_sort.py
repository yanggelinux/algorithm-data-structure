# -*- coding: utf8 -*-


#选择排序


def select_sort(arr):
    """
    选择排序，时间复杂度O(n^2)，空间复杂度O(1)，不稳定排序算法
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(length):
        min_idx = i
        for j in range(i+1,length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
    return arr

if __name__ == '__main__':
    arr = [2,5,4,6,1,3]
    print(select_sort(arr))