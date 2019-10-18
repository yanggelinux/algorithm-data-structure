# -*- coding: utf8 -*-


#桶排序



def bucket_sort(arr):
    """
    桶排序，时间复杂度O(n),空间复杂度O(n)
    arr = [2, 5, 4, 6, 1, 3, 2]
    :param arr:
    :return:
    """
    #初始化桶
    _min = min(arr)
    _max = max(arr)
    buckets = [0 for b in range(_min,_max+1)]
    length = len(arr)
    #遍历数组，在桶的相应索引位置（arr[i] - _min）累加值
    for i in range(length):
        buckets[arr[i] - _min] += 1
    #buckets = [1, 2, 1, 1, 1, 1]
    cur = _min
    n = 0 #list 的计数变量
    #遍历每个桶，对于其元素bkt，若bkt >0 则将其对应的原始数组中的cur依次按照从小到大放入arr
    #cur的取值范围min,min+1,min+2,...,max
    #若i > 1 则说明同一个数出现了不止一次
    for bkt in buckets:
        while bkt > 0:
            arr[n] = cur
            bkt -= 1
            n += 1
        cur += 1
    return arr





if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3, 2]
    print(bucket_sort(arr))
