# -*- coding: utf8 -*-


"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        广度优先，层序遍历，先求出每层的所有元素，再查看又多少层
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        queue = [root]
        res_list = []
        while queue:
            node_list = []
            res = []
            for node in queue:
                res.append(node.val)
                if node.left is not None:
                    node_list.append(node.left)
                if node.right is not None:
                    node_list.append(node.right)
            queue = node_list
            res_list.append(res)
        return len(res_list)

    def maxDepth2(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

    def maxDepth3(self, root):
        """
        深度优先遍历
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, cur_depth = stack.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                stack.append((node.left, cur_depth + 1))
                stack.append((node.right, cur_depth + 1))
        return depth

if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(slt.maxDepth3(root))
