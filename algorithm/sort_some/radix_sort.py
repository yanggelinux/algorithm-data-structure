# -*- coding: utf8 -*-

#基数排序

def radix_sort(arr):
    """
    基数排序
    :param arr:
    :return:
    """
    i = 0 #记录当前正在排哪一位，最低位为1
    _max = max(arr) #最大值
    j = len(str(arr)) #记录最大值的位数

    while i < j:
        buckets = [[] for _ in range(10)] #初始化桶数组
        for x in arr:
            buckets[int(x/(10**i)) % 10].append(x) #找到位置放入桶数组
        arr.clear()
        for x in buckets: #放回原数组
            for y in x:
                arr.append(y)
        i += 1
    return arr

if __name__ == '__main__':
    arr = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    print(radix_sort(arr))
