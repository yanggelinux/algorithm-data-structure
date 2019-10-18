# -*- coding: utf8 -*-


#实现一个二分查找


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

def binary_search2(arr,low,high,target):
    """
    递归方式二分查找
    :param arr:
    :param low:
    :param high:
    :param target:
    :return:
    """
    if low > high:
        return -1
    mid = low +(high - low) // 2
    if arr[mid] == target:
        print("target is:{target},index is {mid}".format(target=arr[mid], mid=mid))
        return mid
    elif arr[mid] < target:
        low = mid + 1
        binary_search2(arr,low,high,target)
    else:
        high = mid - 1
        binary_search2(arr, low, high, target)


#二分查找，查找第一个值等于给定值的元素

def binary_search_some(arr,target):
    """
    二分查找，查找第一个值等于给定值的元素,最后一个值等于给定值的元素
    第一个大于给定值的元素，最后一个小于给定值的元素
    给定值在数组中
    :param arr:
    :param target:
    :return:
    """
    target_index = None
    low,high = 0,len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            target_index = mid
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    if target_index is not None:
        while 1:
            target_index -= 1
            if arr[target_index] < target:
                print("第一个值等于给定值的元素:{},索引:{},最后一个小于给定值的元素:{},索引:{}".format(
                    target,target_index+1,arr[target_index],target_index))
                break
        while 1:
            target_index += 1
            if arr[target_index] > target:
                print("最后一个值等于给定值的元素:{},索引:{},第一个大于给定值的元素:{},索引:{}".format(
                    target, target_index - 1,arr[target_index],target_index))
                break

def binary_search_first(arr,target):
    """
    有序数组有重复值
    查找第一个值等于给定值的元素
    :param arr:
    :param target:
    :return:
    """
    low,high = 0,len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            #arr[mid] == target时
            if mid == 0 or arr[mid -1] != target:
                print("第一个值等于给定值的元素:{}，索引:{}".format(arr[mid],mid))
                return mid
            else:
                low = mid + 1
    return None


def binary_search_last(arr, target):
    """
    有序数组有重复值
    查找最后一个值等于给定值的元素
    :param arr:
    :param target:
    :return:
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            # arr[mid] == target时
            if mid == len(arr) -1 or arr[mid + 1] != target:
                print("最后一个值等于给定值的元素:{}，索引:{}".format(arr[mid], mid))
                return mid
            else:
                low = mid + 1
    return None

def binary_search_first_large(arr,target):
    """
    有序数组有重复值
    查找第一个大于等于给定值的元素
    给定值或许不在数组中
    :param arr:
    :param target:
    :return:
    """
    low, high = 0,len(arr) -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            if mid == 0 or arr[mid-1] < target:
                print("第一个大于等于给定值的元素:{}，索引:{}".format(arr[mid], mid))
                return mid
            else:
                high = mid -1
        else:
            low = mid + 1
    return None

def binary_search_last_less(arr,target):
    """
    有序数组有重复值
    查找最后一个小于等于给定值的元素
    给定值或许不在数组中
    :param arr:
    :param target:
    :return:
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid -1
        else:
            if mid == len(arr) -1 or arr[mid+1] > target:
                print("最后一个小于等于给定值的元素:{}，索引:{}".format(arr[mid], mid))
                return mid
            else:
                low = mid +1
    return None

#一个循环数组[4,5,6,1,2,3],实现一个求给定值的二分查找

def bs(arr,target):
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
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return None

def binary_search_cycle(target):
    """
    一个循环数组[4,5,6,1,2,3],实现一个求给定值的二分查找
    :param target:
    :return:
    """
    arr = [4,5,6,1,2,3]
    i, j = 0, 1
    pivot_index = 0
    length = len(arr)
    while i < length and j < length:
        if arr[i] > arr[j]:
            pivot_index = i
            break
        i += 1
        j += 1
    left_arr = arr[:pivot_index + 1]
    right_arr = arr[pivot_index + 1:]
    left_mid = bs(left_arr, target)
    right_mid = bs(right_arr, target)
    if left_mid is not None and right_mid is None:
        return left_mid
    elif right_mid is not None and left_mid is None:
        return right_mid + len(left_arr)
    else:
        return -1







if __name__ == '__main__':
    arr = [1,3,5,5,7,9,11,13,13,15,17]
    # binary_search(arr,5)
    # binary_search2(arr,0,len(arr)-1, 17)
    # binary_search_some(arr,5)
    # binary_search_first(arr,5)
    # binary_search_last(arr, 5)
    # binary_search_first_large(arr,6)
    # binary_search_last_less(arr,6)
    index = binary_search_cycle(3)
    print(index)