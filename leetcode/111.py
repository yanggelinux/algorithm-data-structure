# -*- coding: utf8 -*-


"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        递归法
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        if left_height <= right_height:
            if left_height > 0:
                return left_height + 1
            else:
                return right_height + 1
        if right_height <= left_height:
            if right_height > 0:
                return right_height + 1
            else:
                return left_height + 1


if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(slt.minDepth(root))