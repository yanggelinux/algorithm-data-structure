# -*- coding: utf8 -*-



#冒泡排序



def bubb_sort(arr):
    """
    冒泡排序，时间复杂度O(n^2)，空间复杂度O(1)，稳定排序算法
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr








if __name__ == '__main__':
    arr = [2,5,4,6,1,3]
    print(bubb_sort(arr))