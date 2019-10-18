# -*- coding: utf8 -*-


#python3.7字典变成有序的了，按照插入的先后顺序
# dd = dict()
# d = {}
# d[1] = "a"
# d[5] = "b"
# d[3] = "c"
# d[4] = "d"
# for k,v in d.items():
#     print(k,v)



def insert_sort(arr):
    """
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(length):
        j = i -1
        value = arr[i]
        while j >=0 and arr[j] > value:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
    return arr

def select_sort(arr):
    """
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


def partition(arr,low,high):
    """
    :param arr:
    :param low:
    :param high:
    :return:
    """
    pivot = arr[low]
    while low < high:
        while arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while arr[low] <= pivot:
            low +=1
        arr[high] = arr[low]
    arr[low] = pivot
    return low

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

def quick_sort(arr,low,high):
    """
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low < high:
        p = partition2(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
    return arr


if __name__ == '__main__':
    arr = [1,4,2,6,5,3,2]
    # print(insert_sort(arr))
    # print(select_sort(arr))
    print(quick_sort(arr,0,len(arr)-1))




