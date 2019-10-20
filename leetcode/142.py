# -*- coding: utf8 -*-


"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        is_cycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
        if is_cycle:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return None

    def detectCycle2(self, head):
        """
        如果我们用一个 Set 保存已经访问过的节点，我们可以遍历整个列表并返回第一个出现重复的节点。
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        if head is None:
            return None
        cur = head
        while cur is not None:
            if cur in s:
                return cur
            s.add(cur)
            cur = cur.next
        return None


if __name__ == '__main__':
    l = ListNode(3)
    l.next = ListNode(2)
    l.next.next = ListNode(0)
    l.next.next.next = ListNode(-4)
    l.next.next.next.next = ListNode(2)
    slt = Solution()
    head = l
    print(slt.detectCycle2(head).val)