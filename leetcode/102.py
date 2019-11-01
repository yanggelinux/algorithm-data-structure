# -*- coding: utf8 -*-


"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
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
            res_list.append(res)
            queue = node_list
        return res_list


if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(11)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(slt.levelOrder(root))