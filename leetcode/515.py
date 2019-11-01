# -*- coding: utf8 -*-



"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res_list = []
        if root is None:
            return res_list
        queue = [root]
        while queue:
            res = []
            node_list = []
            for node in queue:
                res.append(node.val)
                if node.left is not None:
                    node_list.append(node.left)
                if node.right is not None:
                    node_list.append(node.right)
            res_list.append(max(res))
            queue = node_list
        return res_list


if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(slt.largestValues(root))