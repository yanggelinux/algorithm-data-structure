# -*- coding: utf8 -*-


"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.res = []

    def travel(self,root):
        if root is None:
            return
        self.res.append(root.val)
        self.travel(root.left)
        self.travel(root.right)
        print(self.res)

    def invertTree(self, root):
        """
        递归法
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

    def invertTree2(self, root):
        """
        迭代法
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        stack = [root]
        while stack:
            tree_node = stack.pop()
            tmp = tree_node.right
            tree_node.right = tree_node.left
            tree_node.left = tmp
            if tree_node.left is not None:
                stack.append(tree_node.left)
            if tree_node.right is not None:
                stack.append(tree_node.right)
        return root


if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    slt.travel(root)
    root = slt.invertTree2(root)
    slt.travel(root)
