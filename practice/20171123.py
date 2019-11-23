# -*- coding: utf8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        二叉树层次遍历
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res_list = []
        if root is None:
            return res_list
        queue = [root]
        while queue:
            node_list = []
            res = []
            for node in queue:
                if node.left is not None:
                    node_list.append(node.left)
                if node.right is not None:
                    node_list.append(node.right)
                res.append(node.val)
            res_list.append(res)
            queue = node_list
        return res_list

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        possible_list = ["A", "C", "G", "T"]
        queue = [(start,0)]
        visited = []
        while queue:
            word,step = queue.pop(0)
            if word == end:
                return step
            for i in range(len(word)):
                for p in possible_list:
                    temp_word = word[:i] + p + word[i+1:]
                    if temp_word in bank and temp_word not in visited:
                        queue.append((temp_word,step+1))
                        visited.append(temp_word)
        return -1




if __name__ == '__main__':
    slt = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # print(slt.levelOrder(root))
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(slt.minMutation(start,end,bank))
