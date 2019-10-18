# -*- coding: utf8 -*-

#实现一个双链表

#前驱节点是当前节点的上一个节点
#后继节点是当前节点的下一个节点

class DubbleNode(object):
    """
    双链表节点
    """
    def __init__(self,item):
        #节点数据
        self.item = item
        #后继
        self.next = None
        #前驱
        self.prev = None


class DoubleLinkedList(object):
    """
    双链表实现
    """
    def __init__(self,node=None):
        """
        初始化
        :param node:
        """
        self.__head = None

    def is_empty(self):
        """
        是否为空
        :return:
        """
        return self.__head == None

    def length(self):
        """
        链表长度
        :return:
        """
        if self.is_empty():
            return 0
        count = 1
        current = self.__head
        #一直遍历到最后一个节点，最后一个节点指向None
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        # 访问的当前节点
        current = self.__head
        print('[ ', end='')
        while current != None:
            print(current.item, end=' ')
            current = current.next
        print(']')

    def add(self,item):
        """
        链表头部添加节点
        :param item:
        :return:
        """
        #创建新节点
        node = DubbleNode(item)
        #新节点的下一个节点，指向头节点的下一个节点
        node.next = self.__head
        #头节点指向新节点
        self.__head = node
        #新节点下一个节点的前驱节点指向新节点
        node.next.prev = node


    def append(self,item):
        """
        链表尾部添加节点
        :param item:
        :return:
        """
        #创建新节点
        node = DubbleNode(item)
        if self.is_empty():
            #如果是空节点
            self.__head = node
        else:
            current = self.__head
            #找到最后一个节点
            while current.next is not None:
                current = current.next
            #新节点的前驱节点指向当前节点
            node.prev = current
            #当前节点的后继节点指向新节点
            current.next = node

    def insert(self,index,item):
        """
        链表指定位置加入新节点
        :param index:
        :param item:
        :return:
        """
        if index <=0:
            self.add(item)
        elif index > self.length() -1:
            self.append(item)
        else:
            #创建新节点
            node = DubbleNode(item)
            count = 0
            current = self.__head
            #找到要插入的位置
            while count < (index-1):
                count += 1
                current = current.next
            #新节点的后继节点指向当前节点的后继节点
            node.next = current.next
            #当前节点的后继节点指向新节点
            current.next = node
            #新节点的前驱节点指向当前节点
            node.prev = current
            #新节点后继节点的前驱节点指向新节点
            node.next.prev = node

    def remove(self,item):
        """
        根据元素删除链表节点
        :param item:
        :return:
        """
        if self.is_empty():
            return False
        else:
            current = self.__head
            while current.next is not None:
                #找到该节点
                if current.item == item:
                    if current == self.__head:
                        #如果要删除的是头节点
                        self.__head = current.next
                        #如果不是只剩一个点节点
                        if current.next:
                            current.next.prev = None
                    else:
                        #当前节点的上一个节点下一节点指向当前节点的下一个节点
                        current.prev.next = current.next
                        if current.next:
                            #如果不是删除最后一个元素，当前节点的下一个节点的上一个节点指向当前节点的上一个节点
                            current.next.prev = current.prev
                    return
                else:
                    #没有找到，向后移动
                    current = current.next
    def search(self,item):
        """
        查找某元素
        :param item:
        :return:
        """
        if self.is_empty():
            return False
        else:
            current = self.__head
            while current is not None:
                if current.item == item:
                    return True
                else:
                    current = current.next

        return False

if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()

    double_linked_list.append(1)
    double_linked_list.append(2)
    double_linked_list.append(3)
    double_linked_list.travel()
    double_linked_list.insert(0,10)
    double_linked_list.insert(2, 100)
    double_linked_list.travel()
    double_linked_list.remove(100)
    double_linked_list.travel()

