# -*- coding: utf8 -*-



def binary_search(arr,target):
    """
    二分查找
    :param arr:
    :param target:
    :return:
    """
    low,high = 0,len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            print("target is:{target},index is {mid}".format(target=arr[mid],mid=mid))
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return None