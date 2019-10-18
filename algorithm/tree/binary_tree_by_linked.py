# -*- coding: utf8 -*-


#链式存储实现二叉树

class TreeNode(object):
    """
    二叉树的节点
    """
    def __init__(self,data=None,left_node=None,right_node=None):
        self._data = data #存存储的数据
        self.left_node = left_node #左子节点
        self.right_node = right_node #右子节点



class BinaryTree(object):
    """
    二叉树的实现
    """
    def __init__(self):
        self.root = TreeNode()
        self.node_list = []


    def add_node(self,data):
        """
        添加节点,按层添加
        :param data:
        :return:
        """
        #新建树的节点
        node = TreeNode(data)
        #如果树为空，新增的节点为根节点
        if self.root._data is None:
            self.root = node
            self.node_list.append(self.root)
        else:
            tree_node = self.node_list[0]
            #如果树的当前节点没有左子节点，创建左子节点
            if tree_node.left_node is None:
                tree_node.left_node = node
                self.node_list.append(tree_node.left_node)
            else:
                #如果子节点有左子节点，没有右子节点
                tree_node.right_node = node
                self.node_list.append(tree_node.right_node)
                #将该节点从队列中删除
                self.node_list.pop(0)

    def pre_order(self,root):
        """
        前序遍历，递归实现
        :param root:
        :return:
        """
        if root is None:
            return
        print(root._data,end=" ")
        self.pre_order(root.left_node)
        self.pre_order(root.right_node)

    def pre_order2(self,root):
        """
        前序遍历，栈实现
        :param root:
        :return:
        """
        if root is None:
            return
        stack = []
        node = root
        while node or stack:
            #从根节点开始，一只找树的左子节点
            while node:
                print(node._data,end=",")
                stack.append(node)
                node = node.left_node
            #while解释表示当前节点为空，即父节点没有左子节点了
            node = stack.pop()
            #开始查看右子节点
            node = node.right_node


    def in_order(self,root):
        """
        中序遍历，递归实现
        :param root:
        :return:
        """
        if root is None:
            return
        self.in_order(root.left_node)
        print(root._data,end=" ")
        self.in_order(root.right_node)

    def in_order2(self,root):
        """
        中序遍历，栈迭代实现
        :param root:
        :return:
        """
        if root is None:
            return
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left_node
            node = stack.pop()
            print(node._data,end=",")
            node = node.right_node


    def post_order(self,root):
        """
        后序遍历
        :param root:
        :return:
        """
        if root is None:
            return
        self.post_order(root.left_node)
        self.post_order(root.right_node)
        print(root._data,end=",")

    def post_order2(self,root):
        """
        后序遍历，栈迭代实现
        :param root:
        :return:
        """
        if root is None:
            return
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        # 这个while循环的功能是找出后序遍历的逆序，存在stack2里面
        while stack1:
            node = stack1.pop()
            if node.left_node:
                stack1.append(node.left_node)
            if node.right_node:
                stack1.append(node.right_node)
            stack2.append(node)
        while stack2:
            print(stack2.pop()._data,end=",")


    def bsf_order(self,root):
        """
        广度优先遍历
        :param root:
        :return:
        """
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node._data,end=",")
            if node.left_node is not None:
                queue.append(node.left_node)
            if node.right_node is not None:
                queue.append(node.right_node)


    def dsf_order(self,root):
        """
        深度优先遍历
        :param root:
        :return:
        """
        if root is None:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            print(node._data, end=",")
            if node.right_node is not None:
                stack.append(node.right_node)
            if node.left_node is not None:
                stack.append(node.left_node)

if __name__ == '__main__':
    binary_tree = BinaryTree()
    for i in range(10):
        binary_tree.add_node(i)

    binary_tree.pre_order(binary_tree.root)
    print("-")
    binary_tree.pre_order2(binary_tree.root)
    print("-")
    binary_tree.in_order(binary_tree.root)
    print("-")
    binary_tree.in_order2(binary_tree.root)
    print("-")
    binary_tree.post_order(binary_tree.root)
    print("-")
    binary_tree.post_order2(binary_tree.root)
    print("-")
    binary_tree.bsf_order(binary_tree.root)
    print("-")
    binary_tree.dsf_order(binary_tree.root)
    print("-")




