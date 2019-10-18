# -*- coding: utf8 -*-



#计数排序



def count_sort2(arr,k):
    """
    计数排序
    :param arr:
    :param k:
    :return:
    """
    count_arr = [0 for i in range(k+1)] # 临时计数数组
    res_arr = [0 for i in range(len(arr))] #输出数组
    for i in arr:
       count_arr[i] = count_arr[i] + 1
    for j in range(1,len(count_arr)):
        count_arr[j] = count_arr[j] + count_arr[j-1]
    for n in arr:
        res_arr[count_arr[n] -1] = n
        count_arr[n] = count_arr[n] -1
    return res_arr

def count_sort(arr,max_value):
    """
    arr = [2, 5, 4, 6, 1, 3, 2]
    计数排序，时间复杂度O(n+max_value),空间复杂度O(max_value+1)
    :param arr:
    :param max_value:
    :return:
    """
    bucket_length = max_value +1
    bucket = [0 for b in range(bucket_length)]
    sorted_index = 0
    for i in arr:
        if not bucket[i]:
            bucket[i] = 0
        bucket[i] += 1
    # bucket = [0, 1, 2, 1, 1, 1, 1]
    # bucket 的索引表示 arr中元素的值，bucket的值表示arr中拥有该元素的个数
    # arr 中 0 有一个，1有1个，2有2个，3有1个，4有1个，5有1个，6有1个。
    #用索引遍历bucket，
    for j in range(bucket_length):
        while bucket[j] > 0:
            arr[sorted_index] = j
            sorted_index += 1
            bucket[j] -= 1
    return arr








if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3, 2]
    count_sort(arr, 6)