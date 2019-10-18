# -*- coding: utf8 -*-


#关于链表的一些操作

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
    print("]")


#---------链表的环检测-----------
#利用快慢指针，快慢指针的头节点都是head，慢指针走一步，快指针走两步，在不断循环的过程中总会有相遇的时候
#不管链表长度是奇数还是偶数，快慢两指针第一次相遇时总在head节点

def linked_list_has_cycle(head):
    """
    检查链表是否是环链表
    :param head:
    :return:
    """
    if head is None and head.next is None:
        return False
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

def linked_List_get_cycle_node(head):
    """
    找到环链表的入口节点
    :param head:
    :return:
    """
    if head is None and head.next is None:
        return False
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:break
    #如果是环链表
    #如果相遇了，那么把一个指针调整到头部，重新开始再相遇即可
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast



#-------------查找链表的中间节点-------------------
#利用快慢指针,慢指针slow 指向head，快指针fast指向head.next
#慢指针slow每走一步，快指针fast每次走两步，当快指针走向结尾的时候，慢指针正好走向链表中间节点
#如果链表长度为奇数时，中间节点只有一个slow此时的节点
#如果链表长度为偶数时，中间节点有两个 slow 和 slow.next

def linked_list_middle_node(head):
    """
    查找链表的中间节点
    :param head:
    :return:
    """
    if head is None:
        return head
    slow,fast = head,head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

#----------删除链表倒数第n个节点-------------

def linked_list_remove(head,n):
    """
    删除链表倒数第n个节点
    :param head:
    :param n:
    :return:
    """
    if head is None:
        return False
    # 链表长度
    length = 0
    current = head
    #先求出链表长度
    while current is not None:
        length += 1
        current = current.next
    if n > length:
        return False
    else:
        #循环次数
        count = 0
        #前驱节点
        prev = head
        while (length - count)  > (n + 1):
            count += 1
            prev = prev.next

        prev.next = prev.next.next
        return True

def linked_list_remove2(head,n):
    """
    删除链表倒数第n节点方法2,利用两个指针，指针1 先走n 步数
    然后指针2 开始走，当指针1走到尾节点时，指针2正好走到要删除的节点的前一个节点
    :param head:
    :param n:
    :return:
    """
    if head is None:
        return False
    one,two = head,head
    for i in range(n):
        one = one.next
    while one.next is not None:
        one = one.next
        two = two.next
    two.next = two.next.next
    return True

#---------两个有序链表合并-------

def linked_list_merge(head1,head2):
    """
    两个有序链表合并
    :param head1:
    :param head2:
    :return:
    """
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1 is None and head2 is None:
        return None
    new_list = SingleNode()
    current1 = head1
    current2 = head2
    prev = new_list
    while current1 is not None and current2 is not None:
        if current1.item < current2.item:
            prev.next = current1
            current1 = current1.next
        else:
            prev.next = current2
            current2 = current2.next
        prev = prev.next
    if current1 is not None:
        prev.next = current1
    else:
        prev.next = current2
    return new_list.next

if __name__ == '__main__':
    head = create_linked_list(range(9))
    print_linked_list(head)
    print("是否是环链表：",linked_list_has_cycle(head))
    mid_node = linked_list_middle_node(head)
    print(mid_node.item)
    linked_list_remove2(head,2)
    print_linked_list(head)
    head1 = create_linked_list([1,5,9])
    head2 = create_linked_list([2, 3, 4, 10, 12])
    new_head = linked_list_merge(head1, head2)
    print_linked_list(new_head)
