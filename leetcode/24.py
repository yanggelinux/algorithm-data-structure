# -*- coding: utf8 -*-


"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p_head = ListNode(None)
        p_head.next = head
        prev_head = p_head
        while prev_head.next is not None and prev_head.next.next is not None:
            tmp1 = prev_head.next
            tmp2 = prev_head.next.next
            prev_head.next = tmp2
            tmp1.next = tmp2.next
            tmp2.next = tmp1
            prev_head = prev_head.next.next
        return p_head.next






if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    iter_list(l)
    head = l
    slt = Solution()
    l2 = slt.swapPairs(head)
    iter_list(l2)