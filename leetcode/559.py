# -*- coding: utf8 -*-


"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :

       1
     / ｜ \
   3   2  4
  / \
 5  6


我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。

"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        广度优先，层序遍历
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        res_list = []
        queue = [root]
        while queue:
            res = []
            node_list = []
            for node in queue:
                res.append(node.val)
                if node.children:
                    node_list.extend(node.children)
            queue = node_list
            res_list.append(res)
        return len(res_list)

    def maxDepth2(self, root):
        """
        深度优先
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root,1)]
        depth = 0
        while stack:
            node,cur_depth = stack.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                for child_node in node.children:
                    stack.append((child_node,cur_depth +1))
        return depth


if __name__ == '__main__':
    slt = Solution()
    root = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    node5 = Node(5, [])
    node6 = Node(6, [])
    node3.children.append(node5)
    node3.children.append(node6)
    root.children.append(node3)
    root.children.append(node2)
    root.children.append(node4)
    print(slt.maxDepth2(root))