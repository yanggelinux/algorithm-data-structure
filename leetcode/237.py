# -*- coding: utf8 -*-


"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:



 

示例 1:

输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
"""

def iter_list(l):
    cur = l
    while cur.next is not None:
        print(cur.val,end="->")
        cur = cur.next
    print(cur.val)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        思路就是把下一个节点的值赋给当前节点，然后将当前节点指向下下个节点
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class Solution2(object):
    def deleteNode(self,head,node):
        """
        思路就是把下一个节点的值赋给当前节点，然后将当前节点指向下下个节点
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if head is None:
            return
        cur = head
        while cur is not None and cur.next is not None:
            if cur.next.val == node.val:
                cur.next = cur.next.next
            cur = cur.next
        return head



if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(6)
    iter_list(l)
    slt = Solution2()
    node = ListNode(3)
    head = l
    l2=slt.deleteNode(head,node)
    iter_list(l2)

