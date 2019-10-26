# -*- coding: utf8 -*-





def get_not_order(arr):
    """
    求逆序度，遍历数组中每个元素，分别找出别他小的数为k，所有k的和就是一个数组的逆序度
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                print((arr[i],arr[j]))


MAX_W = 100

def get_stone(i,cw,w,items,n):
    """
    假设背包可承受重量 100，物品个数 10，物品重量存储在数组 a 中，那可以这样调用函数：
    f(i=0,cw=0,w=100,items=[],n=10)
    :param i: 表示考察到哪个物品了
    :param cw: 表示当前装进包里的物品重量的和
    :param w: 背包重量
    :param items:每个物品重量的数组
    :param n:物品个数
    :return:
    """
    if i == n or cw == w: #cw==w 表示装满了 ;i==n 表示已经考察完所有的物品
        if cw > MAX_W:
            # MAX_W=cw
            return
    get_stone(i+1,cw,w,items,n) #当前物品不装进背包
    if cw + items[i] <= w:
        get_stone(i + 1, cw+items[i], w, items, n)






if __name__ == '__main__':
    arr = [2,4,3,1,5,6]
    get_not_order(arr)
    items = [10,20,30,40,50,60,70,80,90,100]
    get_stone(i=0, cw=0, w=100, items=items, n=10)