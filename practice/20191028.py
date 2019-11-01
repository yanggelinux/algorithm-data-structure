# -*- coding: utf8 -*-


"""
-----------------------------------------------------------------------------
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
--------------------------------------------
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseString(self, s):
        """
        迭代的方式
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n -1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i +=1
            j-=1
        return s

    def reverseString2(self, s):
        """
        递归的方式
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        def helper(i,j):
            if i >= j:
                return
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            helper(i,j)

        n = len(s)
        i = 0
        j = n - 1
        helper(i,j)
        return s
    def travel_linked_list(self,head):
        """
        遍历链表
        :param head:
        :return:
        """
        if head is None:
            return
        cur = head
        while cur.next is not None:
            print(cur.val,end="->")
            cur = cur.next
        print(cur.val)


    def swapPairs(self, head):
        """
        递归法recursion
        给定 1->2->3->4, 你应该返回 2->1->4->3.
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next





if __name__ == '__main__':
    slt = Solution()
    # s = ["H","a","n","n","a","h"]
    # print(slt.reverseString2(s))
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    slt.travel_linked_list(head)
    head = slt.swapPairs(head)
    slt.travel_linked_list(head)
