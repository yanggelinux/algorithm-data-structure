# -*- coding: utf8 -*-





def heap_insert(heap,elem):
    """
    往堆中插入一个元素
    :param heap:
    :param elem:
    :return:
    """
    if len(heap) == 0:
        heap.append(0)
    heap.append(elem)
    i = len(heap) -1
    while i // 2 > 0 and heap[i] >= heap[i//2]:
        heap[i],heap[i//2] = heap[i//2],heap[i]
        i = i//2

    print(heap)

def heap_delete_top(heap):
    """
    删除堆顶元素
    :param heap:
    :return:
    """
    if len(heap) == 1:
        return
    heap[1] = heap[-1]
    heap.pop()
    n = len(heap)-1
    i = 1
    while 1:
        max_pos = i
        if i*2 < n and heap[i] < heap[i*2]:max_pos=i*2
        if i*2+1 < n and heap[max_pos] < heap[i*2+1]:max_pos=i*2+1
        if max_pos == i:break
        heap[i],heap[max_pos] = heap[max_pos],heap[i]
        i = max_pos
    print(heap)



def build_heap(arr):
    """
    创建堆
    :param arr:
    :return:
    """
    n = len(arr) -1
    print("length",n)
    for i in range(n//2,0,-1):
        heapify(arr, n, i)
    print(arr)

def heapify(arr,n,i):
    """
    从上到下堆化
    :param arr:
    :param n:
    :param i:
    :return:
    """
    while 1:
        max_pos = i
        if i*2 <= n and arr[i] < arr[i*2]:max_pos=i*2
        if i*2+1 <= n and arr[max_pos] < arr[i*2+1]:max_pos=i*2+1
        if max_pos == i:break
        arr[i],arr[max_pos] = arr[max_pos],arr[i]
        i = max_pos

def heap_sort(heap):
    """
    堆排序
    :param heap:
    :return:
    """
    n = len(heap) -1
    k = n
    while k >1:
        heap[1],heap[k] = heap[k],heap[1]
        k -= 1
        heapify(heap,k,1)
    print(heap)


if __name__ == '__main__':
    heap = [0,33,17,21,16,13,15,9,5,6,7,8,1,2]
    elem = 22
    heap_insert(heap, elem)
    heap = [0, 33, 27, 21, 16, 13, 15, 19, 5, 6, 7, 8, 1, 2,12]
    heap_delete_top(heap)
    # arr = [0, 7, 27, 8, 16, 12, 15, 19, 5, 6, 33, 21, 1, 2,13]
    arr = [0,1,2,5,6,7,8,12,13,15,16,19,21,27,33]
    build_heap(arr)
    heap_sort(heap)

