# -*- coding: utf8 -*-


"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.p_list = []
        self.q_list = []

    def pre_order(self, root, res_list):
        """
        二叉树前序遍历
        :param root:
        :param res_list:
        :return:
        """
        if root is None:
            res_list.append(None)
            return
        res_list.append(root.val)
        self.pre_order(root.left, res_list)
        self.pre_order(root.right, res_list)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.pre_order(p, self.p_list)
        self.pre_order(q, self.q_list)
        return self.p_list == self.q_list

if __name__ == '__main__':
    slt = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.left = TreeNode(2)
    slt.isSameTree(p,q)