# -*- coding: utf8 -*-


#python数组实现lru算法
def lru_by_array(item,arr):
    """
    总的时间复杂度O(n^2)
    :param item:
    :param arr:
    :return:
    """
    for i in range(len(arr) -1): #时间复杂度O(n)
        if arr[i] == item:
            #如果列表里面有该元素，删除该元素并方到列表的头部
            arr.pop(i) #时间复杂度O(n)
            arr.insert(0,item) #时间复杂度O(n)
            break
    else:
        #如果列表里面没有该元素，直接将该元素添加到列表头部
        arr.insert(0, item) #时间复杂度O(n)
    return arr


if __name__ == '__main__':
    item = 2
    arr = [1,2,3,4,5,6,7,8,9]
    res = lru_by_array(item, arr)
    print(res)
