# -*- coding: utf8 -*-


#归并排序


def merge_sort(arr):
    """
    归并排序，时间复杂度O(nlogn)，空间复杂度O(n),稳定排序算法
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr,right_arr)

def merge(left_arr,right_arr):
    """

    :param left_arr:
    :param right_arr:
    :return:
    """
    result = []
    while 1:
        if left_arr and right_arr:
            if left_arr[0] > right_arr[0]:
                min_nun,right_arr = right_arr[0],right_arr[1:]
            else:
                min_nun,left_arr = left_arr[0],left_arr[1:]
        elif left_arr and not right_arr:
            min_nun, left_arr = left_arr[0], left_arr[1:]
        elif right_arr and not left_arr:
            min_nun, right_arr = right_arr[0], right_arr[1:]
        else:
            break
        result.append(min_nun)
    return result

if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3]
    print(merge_sort(arr))