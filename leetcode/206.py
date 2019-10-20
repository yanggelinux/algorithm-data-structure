# -*- coding: utf8 -*-



"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def iter_list(l):
    cur = l
    while cur.next is not None:
        print(cur.val,end="->")
        cur = cur.next
    print(cur.val)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = head
        tmp = None
        new_head = None
        while cur is not None:
            tmp = cur.next
            cur.next = new_head
            new_head = cur
            cur = tmp
        return new_head



if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    iter_list(l)
    head = l
    slt = Solution()
    l2 = slt.reverseList(head)
    iter_list(l2)