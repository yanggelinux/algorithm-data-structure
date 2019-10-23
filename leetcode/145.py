# -*- coding: utf8 -*-


"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
﻿后序遍历：对于树中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印它本身。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        递归法
        :type root: TreeNode
        :rtype: List[int]
        """
        res_list = []
        if root is None:return res_list
        res_left_list = self.postorderTraversal(root.left)
        res_list += res_left_list
        res_right_list = self.postorderTraversal(root.right)
        res_list += res_right_list
        res_list.append(root.val)
        return res_list

    def postorderTraversal2(self, root):
        """
        递归法
        :type root: TreeNode
        :rtype: List[int]
        """
        res_list = []
        if root is None: return res_list
        stack = [root]
        stack1 = []
        while stack:
            tree_node = stack.pop()
            #先检查左子节点，进栈
            if tree_node.left is not None:
                stack.append(tree_node.left)
            #再检查右子节点进栈
            if tree_node.right is not None:
                stack.append(tree_node.right)
            #获取stack1 的反序
            stack1.append(tree_node)
        while stack1:
            res_list.append(stack1.pop().val)
        return res_list

    def postorderTraversal3(self, root):
        """
        迭代法，标记颜色
        :type root: TreeNode
        :rtype: List[int]
        """
        white,grey = 0,1
        res_list = []
        if root is None: return res_list
        stack = [(white,root)]
        while stack:
            color,tree_node = stack.pop()
            if tree_node is None:continue
            if color == white:
                #入栈方式，正好和 递归方式的顺序相反。
                stack.append((grey,tree_node))
                stack.append((white,tree_node.right))
                stack.append((white,tree_node.left))
            else:
                res_list.append(tree_node.val)
        return res_list




if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(slt.postorderTraversal3(root))