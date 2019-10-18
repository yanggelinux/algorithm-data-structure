# -*- coding: utf8 -*-

#实现一个单向循环链表

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

class SingleCircleLinkedList(object):
    """
    单向循环链表
    """
    def __init__(self,node=None):
        self.__head = None
        if node:
            #不是构造空的链表
            #头节点的下一个节点指向头节点
            node.next = node


    def is_empty(self):
        """
        链表是否为空
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
        #当前节点的下一节点不是都节点
        while current.next != self.__head:
            count += 1
            #节点后移
            current = current.next
        return count

    def travel(self):
        """
        遍历列表
        :return:
        """
        if self.is_empty():
            return  False
        current = self.__head
        print('[ ', end='')
        while current.next != self.__head:
            print(current.item, end=' ')
            current = current.next
        #打印最后一个元素
        print(current.item, end=' ')
        print(']')

    def add(self,item):
        """
        链表头部添加节点
        :param item:
        :return:
        """
        node = SingleNode(item)
        if self.is_empty():
            #空链表
            self.__head = node
            node.next = node
        else:
            #非空链表头部添加节点
            current = self.__head
            #找到最后一个节点
            while current.next != self.__head:
                current = current.next
            #新节点的下一个节点是头节点
            node.next = self.__head
            #新链表的头节点为新节点
            self.__head = node
            #最后一个节点的下一个节点为新节点（头节点）
            current.next = node

    def append(self,item):
        """
        链表尾部添加新节点
        :param item:
        :return:
        """
        node = SingleNode(item)
        if self.is_empty():
            #空链表
            self.__head = node
            node.next = node
        else:
            #非空链表
            current = self.__head
            #找到最后一个节点
            while current.next != self.__head:
                current = current.next
            #最后一个节点的下一个节点是新节点
            current.next = node
            #新节点的下一个节点是头节点
            node.next = self.__head

    def insert(self,index,item):
        """
        链表指定位置插入新节点
        :param index:
        :param item:
        :return:
        """
        if index <= 0:
            #链表头部插入
            self.add(item)
        elif index > self.length() -1:
            #链表尾部加入
            self.append(item)
        else:
            #创建新节点
            node = SingleNode(item)
            #遍历次数
            count = 0
            #插入位置的前驱节点
            prev = self.__head
            while count < (index -1):
                count += 1
                prev = prev.next
            #新节点的下一个节点为前驱节点的下一个节点
            node.next = prev.next
            #前驱节点的下一个节点为新节点
            prev.next = node

    def remove(self,item):
        """
        根据元素删除节点
        :param item:
        :return:
        """
        if self.is_empty():
            return False

        current = self.__head
        prev = None
        while current.next != self.__head:
            if  current.item == item:
                #找到要删除的节点
                if current == self.__head:
                    #如果要删除的节点是头节点，先找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    #头节点指向当前节点的下一个节点
                    self.__head = current.next
                    #尾节点指向头节点
                    rear.next = self.__head
                else:
                    #要删除的节点是中间节点，上一个节点的下一个节点指向当前节点的下一个节点
                    prev.next = current.next
            else:
                #没有找到，向后移动
                prev = current
                current = current.next
        #循环结束current 指向尾节点
        if current.item == item:
            if prev:
                #如果删除的是最后一个节点
                prev.next = current.next
            else:
                #删除只含有一个头节点的链表的头节点
                self.head = None
    def search(self,item):
        """
        链表查找元素
        :param item:
        :return:
        """
        if self.is_empty():
            return False
        current = self.__head
        while current.next != self:
            if current.item == item:
                return True
            else:
                current = current.next
        #最后一个节点
        if current.item == item:
            return True
        return False
    def get_head(self):
        """
        获取头节点
        :return:
        """
        return self.__head

def linked_list_has_cycle(head):
    """
    检查链表是否是环链表
    :param head:
    :return:
    """
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

def linked_List_get_cycle_node(head):
    if head is None and head.next is None:
        return False
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            print(111,slow.item,fast.item)
            break
    #如果是环链表
    #如果相遇了，那么把一个指针调整到头部，重新开始再相遇即可
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast

if __name__ == '__main__':
    single_circle_linked_list = SingleCircleLinkedList()
    print("--是否为空：",single_circle_linked_list.is_empty())
    print("--链表长度：",single_circle_linked_list.length())
    single_circle_linked_list.add(10)
    single_circle_linked_list.append(0)
    single_circle_linked_list.append(1)
    single_circle_linked_list.append(2)
    single_circle_linked_list.insert(0,100)
    single_circle_linked_list.travel()
    single_circle_linked_list.remove(100)
    single_circle_linked_list.travel()
    print("--查找：",single_circle_linked_list.search(10))
    head = single_circle_linked_list.get_head()
    print("是否是环链表：", linked_list_has_cycle(head))
    cycle_node = linked_List_get_cycle_node(head)
    print(cycle_node.item)

