# -*- coding: utf8 -*-

#实现单链表反转


# 1、首先定义一个 new_head 保存前一个结点，current 保存当前结点，然后还有一个 tmp 临时保存下一个结点，其中 new_head 就是最终的反转链表的头结点；
# 2、先让 tmp 保存下一个结点 tmp = current.next；
# 3、然后改变 current 的 next 指针，指向前一个结点，即 current.next = new_head (当current为头节点时，此时原链表的头节点下一节点为空) ;
# 4、接着，让 new_head = current  ；
# 5、最后，就是让 current = tmp(current = current.next)，指向下一个结点
# 6、重复 2-5 步，直到当前结点为空


class SingleNode(object):
    """
    链表的节点
    """
    def __init__(self,item=None):
        """
        初始化需要传入节点的数据
        :param data:
        """
        self.item = item
        self.next = None


def create_linked_list(arr):
    """
    根据一个列表中元素创建链表,返回头节点
    :param arr:
    :return:
    """
    node = SingleNode()
    current = node
    for i in arr:
        current.next = SingleNode(i)
        current = current.next
    return node.next


def print_linked_list(head):
    """
    根据头节点打印出整个列表
    :param head:
    :return:
    """
    current = head
    print("[",end=" ")
    while current is not None:
        print(current.item,end=" ")
        current = current.next
    print("]", end=" ")


def reverse_linked_list(head):
    """
    根据头节点反转列表
    :param head:
    :return:
    """
    #如果头节点为None或者链表只有一个元素 直接返回头节点
    if head is None or head.next is None:
        return head
    #当前节点
    current = head
    #保存数据的临时变量
    tmp = None
    #新的翻转单链表的节点头
    new_head = None
    while current is not None:
        tmp = current.next
        current.next = new_head
        new_head = current
        current = tmp
    return new_head

def reverse_linked_list2(head):
    """
    递归的方式反转链表
    :param head:
    :return:
    """
    # 如果头节点为None或者链表只有一个元素 直接返回头节点
    if head is None or head.next is None:
        return head
    else:
        new_head = reverse_linked_list2(head.next)
        head.next.next = head
        head.next = None
    return new_head


if __name__ == '__main__':
    head = create_linked_list(range(5))
    print_linked_list(head)
    new_head = reverse_linked_list(head)
    print_linked_list(new_head)
    new_head = reverse_linked_list2(new_head)
    print_linked_list(new_head)