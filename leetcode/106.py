# -*- coding: utf8 -*-

"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        二叉树后序遍历结果最后一个元素是二叉树的根元素
        二叉树中序遍历结果，根元素左边是左子树元素，根元素右面是右子树元素
        递归构建二叉树
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_idx],postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:],postorder[root_idx:-1])
        return root


if __name__ == '__main__':
    slt = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    slt.buildTree(inorder,postorder)
