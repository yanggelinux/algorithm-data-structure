# -*- coding: utf8 -*-


"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        二叉树前序遍历的列表第一个元素是根元素
        中序遍历的列表根元素的左边是左子树的元素，右边是右子树的元素
        利用递归，构建二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_idx+1],inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:],inorder[root_idx+1:])
        return root


if __name__ == '__main__':
    slt = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    slt.buildTree(preorder, inorder)
