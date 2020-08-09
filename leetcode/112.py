# -*- coding: utf8 -*-

"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        num = 0
        if root is None:
            return False
        stack = [(root, num + root.val)]
        while stack:
            tree_node, num = stack.pop()
            if tree_node.left is None and tree_node.right is None and num == sum:
                return True
            if tree_node.left is not None:
                stack.append([tree_node.left, num + tree_node.left.val])
            if tree_node.right is not None:
                stack.append([tree_node.right, num + tree_node.right.val])
        return False


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    slt = Solution()
    sum = 22
    print(slt.hasPathSum(root, sum))
