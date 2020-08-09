# -*- coding: utf8 -*-



"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res_list = []
        if root is None:
            return res_list
        queue = [root]
        while queue:
            res = []
            node_list = []
            for tree_node in queue:
                res.append(tree_node.val)
                if tree_node.left is not None:
                    node_list.append(tree_node.left)
                if tree_node.right is not None:
                    node_list.append(tree_node.right)
            queue = node_list
            res_list.append(res)
        return res_list[::-1]





if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(slt.levelOrderBottom(root))