# -*- coding: utf8 -*-


"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        try:
            cur1 = head
            cur2 = head.next
            while cur1 is not None and cur2 is not None:
                if cur1 == cur2:
                    return True
                cur1 = cur1.next
                cur2 = cur2.next.next
            return False
        except Exception:
            return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle3(self, head):
        """
        我们可以通过检查一个结点此前是否被访问过来判断链表是否为环形链表。常用的方法是使用哈希表。
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        if head is None :
            return False
        cur = head
        while cur is not None:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False



if __name__ == '__main__':
    l = ListNode(3)
    l.next = ListNode(2)
    l.next.next = ListNode(0)
    l.next.next.next = ListNode(-4)
    l.next.next.next.next = ListNode(2)
    slt = Solution()
    head = l
    print(slt.hasCycle3(head))