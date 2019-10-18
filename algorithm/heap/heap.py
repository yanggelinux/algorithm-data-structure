# -*- coding: utf8 -*-




class BigTopHeap(object):
    """
    实现一个大顶堆
    """
    def __init__(self,data=None):
        """
        初始化堆
        """
        self._data = [0]
        if isinstance(data,list):
            self._data = self._data + data

    def _heapify(self,n,i):
        """
        堆化
        :param n:
        :param i:
        :return:
        """
        self._heap_down(self._data,n,i)

    def _heap_down(self,data,n,i):
        """
        自上而下堆化
        :return:
        """
        while 1:
            max_pos = i
            if i * 2 <= n and data[i] < data[i * 2]: max_pos = i * 2
            if i * 2 + 1 <= n and data[max_pos] < data[i * 2 + 1]: max_pos = i * 2 + 1
            if max_pos == i: break
            data[i], data[max_pos] = data[max_pos],data[i]
            i = max_pos

    def build_heap(self):
        """
        创建一个堆
        :return:
        """
        n = len(self._data) - 1
        for i in range(n // 2, 0, -1):
            self._heapify(n,i)

    def insert(self,val):
        """
        往堆中插入一个元素
        :param val:
        :return:
        """
        if len(self._data) < 1:
            self._data.append(0)
        self._data.append(val)
        i = len(self._data) -1
        while i // 2 > 0 and self._data[i] >= self._data[1//2]:
            self._data[i], self._data[i // 2] = self._data[i // 2], self._data[i]
            i = i // 2

    def remove_top(self):
        """
        删除堆顶元素
        :return:
        """
        if len(self._data) == 1:
            return False
        self._data[1] = self._data[-1]
        self._data.pop()
        i = 1
        n = len(self._data) -1
        self._heapify(n,i)
        return True

    def get_heap_top(self):
        """
        获取堆顶元素
        :return:
        """
        if len(self._data) == 1:
            raise Exception("heap is empty")
        return self._data[1]

    def sort(self):
        """
        排序
        :return:
        """
        n = len(self._data) - 1
        k = n
        while k > 1:
            self._data[1], self._data[k] = self._data[k], self._data[1]
            k -= 1
            self._heapify(k, 1)

    def __repr__(self):
        return str(self._data)


if __name__ == '__main__':
    data = [1,2,5,6,7,8,12,13,15,16,19,21,27,33]
    big_top_heap = BigTopHeap(data)
    big_top_heap.build_heap()
    print(big_top_heap)
    big_top_heap.insert(36)
    print(big_top_heap)
    big_top_heap.remove_top()
    print(big_top_heap)
    print(big_top_heap.get_heap_top())
    big_top_heap.sort()
    print(big_top_heap)



