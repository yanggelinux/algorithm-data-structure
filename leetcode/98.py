# -*- coding: utf8 -*-


"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
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

    def in_order(self,root):
        if root is None:
            return
        self.in_order(root.left)
        self.res.append(root.val)
        self.in_order(root.right)
        return self.res


    def isValidBST(self, root):
        """
        利用二叉搜索树中序遍历结果是有序序列这个特性判断
        :type root: TreeNode
        :rtype: bool
        """
        self.in_order(root)
        #如果中序遍历的结果有重复值，先去重后排序，再比较
        return self.res == sorted(list(set(self.res)))

    def isValid(self,root,low = float('-inf'), high = float('inf')):
        """

        :param root:
        :param low:
        :param high:
        :return:
        """
        if root is None:
            return True
        if root.val <= low or root.val >= high:
            return False
        if not self.isValid(root.right,root.val,high):return False
        if not self.isValid(root.left,low,root.val):return False
        return True

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        二叉搜索树，左子树所有节点比节点小，右子树所有比节点大，
        """
        return self.isValid(root)



if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(7)
    # root.right.right = TreeNode(9)
    print(slt.isValidBST2(root))