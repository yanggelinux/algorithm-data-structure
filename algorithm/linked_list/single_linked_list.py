# -*- coding: utf8 -*-

#实现一个单链表

class SingleNode(object):
    """
    链表的节点
    """
    def __init__(self,item):
        """
        初始化需要传入节点的数据
        :param data:
        """
        self.item = item
        self.next = None

class SingleLinkedList(object):
    """
    单链表类
    """
    def __init__(self):
        """
        初始化，头节点为空
        """
        self.__head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head == None

    def length(self):
        """
        获取链表长度
        :return:
        """
        count = 0
        current = self.__head
        while current is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """
        遍历整个链表
        :return:
        """
        current = self.__head
        print('[ ', end='')
        while current is not None:
            print(current.item, end=' ')
            current = current.next
        print(']')

    def add(self,item):
        """
        往链表头部添加元素
        :return:
        """
        node = SingleNode(item)
        #新节点的后继节点为旧链表的头节点
        node.next = self.__head
        #新链表的头节点为新节点
        self.__head = node

    def append(self,item):
        """
        链表尾部添加元素
        :param item:
        :return:
        """
        node = SingleNode(item)
        if self.is_empty():
            #节点为空时，链表头节点为新节点
            self.__head = node
        else:
            #让指针指向最后节点
            current = self.__head
            #单链表最后一个节点next 为None
            while current.next is not None:
                current =  current.next
            #在最后一个节点的下一个节点为新添加的节点
            current.next = node

    def insert(self,index,item):
        """
        指定位置插入元素
        :param index:
        :param item:
        :return:
        """
        if index <=0:
            #头部添加
            self.add(item)
        elif index > (self.length() -1):
            #尾部添加
            self.append(item)
        else:
            #创建新节点
            node = SingleNode(item)
            #遍历次数，通过count 遍历的次数 找到index
            count = 0
            #要插入位置的前驱节点
            prev = self.__head
            while count < (index -1):
                count += 1
                prev = prev.next
            #新节点的后继节点为前驱节点的后继节点
            node.next = prev.next
            #前驱节点的后继节点为新节点
            prev.next = node

    def remove(self,item):
        """
        通过元素删除链表节点
        :param item:
        :return:
        """
        current = self.__head
        prev = None
        while current is not None:
            if current.item == item:
                if not prev:
                    #如果没有前驱节点，比如删除头节点
                    self.__head = current.next
                else:
                    #前驱节点的下一个节点指向当前节点的下一个节点
                    prev.next = current.next
                return
            else:
                #没找到，往后移动
                prev = current
                current = current.next
    def search(self,item):
        """
        查找节点是否存在
        :param item:
        :return:
        """
        current = self.__head
        while current is not None:
            if current.item == item:
                return True
            else:
                #向后移动查找
                current = current.next
        return False

    def get_head(self):
        """
        获取头节点
        :return:
        """
        return self.__head

def reverse(linked_list):
    """
    链表反转
    :return:
    """
    head = linked_list.get_head()
    new_head = None
    if head is None or head.next is None:
        return linked_list
    while head is not None:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    return new_head






if __name__ == '__main__':
    single_linked_list = SingleLinkedList()
    single_linked_list.append(0)
    single_linked_list.append(1)
    single_linked_list.append(2)
    single_linked_list.append(3)
    single_linked_list.append(4)
    single_linked_list.append(5)
    single_linked_list.travel()
    new_head = reverse(single_linked_list)
    while new_head is not None:
        print(new_head.item)
        new_head = new_head.next
