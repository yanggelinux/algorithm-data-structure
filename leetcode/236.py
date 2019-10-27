# -*- coding: utf8 -*-

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

    3
  /  \
  5    1
 / \  / \
6  2 0  8
   /\
  7 4
 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

﻿用数组来存储，对于完全二叉树，如果节点x存储的下标为i，那么他的左子节点的存储下标为2*i，
右子节点的下标为2*i+1，反过来下标i/2存储的位置就是该节点的父节点，注意跟节点存储在下标为1的位置。
完全二叉树用数组来存储时是最节省内存的方式。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        node_list = [0]
        queue = [root]
        while queue:
            tree_node = queue.pop(0)
            node_list.append(tree_node.val)
            if tree_node.left is not None:
                queue.append(tree_node.left)
            else:
                node_list.append(None)
            if tree_node.left is not None:
                queue.append(tree_node.right)
            else:
                node_list.append(None)
            print(tree_node.val)
        print(node_list)



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    slt = Solution()
    slt.lowestCommonAncestor(root,TreeNode(5),TreeNode(1))