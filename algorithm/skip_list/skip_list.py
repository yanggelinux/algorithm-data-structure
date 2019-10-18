# -*- coding: utf8 -*-

import random

#实现一个跳表

class SkipListNode(object):
    """
    跳表的节点
    """
    def __init__(self,val,high=1):
        #节点存储的值
        self.data = val
        #节点对应索引层的深度
        self.deeps = [None] * high


class SkipList(object):
    """
    实现跳表
    """

    def __init__(self):
        #索引层的最大深度
        self._MAX_LEVEL = 16
        #跳表的高度
        self._high = 1
        #每一索引层的首节点，默认值为None
        self._head = SkipListNode(None,self._MAX_LEVEL)


    def random_level(self,p=0.25):
        """
        确定要插入索引层的随机函数
        :param p:
        :return:
        """
        high = 1
        for _ in range(self._MAX_LEVEL -1):
            if random.random() < p:
                high += 1
        return high

    def insert(self,val):
        """
        跳表插入元素，插入时通过随机函数获取要更新的索引层数，
        要多低于给定高度的索引层添加新的节点指针
        :param val:
        :return:
        """

        high = self.random_level()
        if self._high < high:
            self._high = high
        #创建新节点
        new_node = SkipListNode(val,high)
        #cache 用来缓存对应索引层中小于插入值的最大节点
        cache = [self._head] * high
        #当前指针位置，指向首节点
        cur = self._head
        #在低于随机高度的每一个索引层寻找小于插入值的节点
        for i in range(high-1,-1,-1):
            # 每个索引层内寻找小于待插入值的节点
            # 索引层上下是对应的，下层的起点是上一索引层中小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        #在小于高度的每个索引层中插入新节点
        for i in range(high):
            # new.next = prev.next \ prev.next = new.next
            new_node.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = new_node

    def find(self,val):
        """
        跳表中，查找给定的值
        :param val:
        :return:
        """
        cur = self._head
        print(self._high)
        #从索引的顶层，逐层定位要查找的值
        #索引层是上下对应的，下层起点是上一个索引层中小于插入值的最大值对应的节点
        for i in range(self._high-1,-1,-1):
            #同一索引层内，查找小于插入值的最大值对应的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def delete(self,val):
        """
        跳表中删除给定值
        要将每个索引层中对应的节点都删掉
        :param val:
        :return:
        """
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._high
        cur = self._head
        #缓存每一个索引层小于插入值的节点
        for i in range(self._high-1,-1,-1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        #如果给定的值存在，删除每个索引层中对应的节点
        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]


    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return "->".join(vals)

    def test(self):
        p = self._head
        # for deep in p.deeps:
        #     if deep:
        #         print(deep.data,deep.deeps)
        print (p.deeps[0].data)
        print(p.deeps[0].deeps[0].data)


if __name__ == '__main__':
    skip_list = SkipList()
    for i in range(1,11):
        skip_list.insert(i)
    print(skip_list)
    p = skip_list.find(7)
    print(p.data)
    skip_list.delete(4)
    print(skip_list)
    skip_list.test()