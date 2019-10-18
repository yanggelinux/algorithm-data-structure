# -*- coding: utf8 -*-


#实现二叉查找树

class TreeNode(object):
    """
    树的节点
    """
    def __init__(self, data=None, left_node=None, right_node=None,parent_node=None):
        self._data = data  # 存存储的数据
        self.left_node = left_node  # 左子节点
        self.right_node = right_node  # 右子节点
        self.parent_node = parent_node


class BinarySearchTree(object):
    """
    实现二叉查找树
    """
    def __init__(self):
        self.root = None

    def add(self,data):
        """
        增加节点
        :param data:
        :return:
        """
        new_node = TreeNode(data)
        #如果树为空
        if self.root is None:
            self.root = new_node
        else:
            tree_node = self.root
            while tree_node is not None:
                #如果要插入的值大于等于节点数据，遍历右子树，将值插入到右子树中
                if data >= tree_node._data:
                    if tree_node.right_node is None:
                        tree_node.right_node = new_node
                        new_node.parent_node = tree_node
                        return
                    tree_node = tree_node.right_node
                else: #要插入的值小于节点的数据，遍历左子树，将节点插入左子树
                    if tree_node.left_node is None:
                        tree_node.left_node = new_node
                        new_node.parent_node = tree_node
                        return
                    tree_node = tree_node.left_node

    def search(self,data):
        """
        根据数据查找节点，如果又相同的数据都查出来
        :param data:
        :return:
        """
        res = []
        if self.root is None:
            return res
        else:
            tree_node = self.root
            while tree_node is not None:
                if data >= tree_node._data:
                    if tree_node._data == data:
                        res.append(tree_node)
                    tree_node = tree_node.right_node

                else:
                    tree_node = tree_node.left_node
        return res


    def delete(self,data):
        """
        找到数据，删除节点，如果又数据相同的节点都删除
        :param data:
        :return:
        """
        if self.root is None:
            return
        del_list = self.search(data)
        for node in del_list:
            #父节点为空，又不是根节点，已经不在树上不需要删除
            if node.parent_node is None and node != self.root:
                continue
            else:
                self._del(node)

    def _del(self,node):
        """
        删除操作
        :param node:
        :return:
        """
        #如果要删除的节点没有子节点
        if node.left_node is None and node.right_node is None:
            #要删除的是根节点
            if node == self.root:
                self.root = None
            else:
                if node._data < node.parent_node._data:
                    node.parent_node.left_node = None
                else:
                    node.parent_node.right_node = None
                node.parent_node = None
        #左节点不存在，右节点存在
        elif node.left_node is None and node.right_node is not None:
            if node == self.root:
                self.root = node.right_node
                self.root.parent_node = None
                node.left_node = None
            else:
                if node._data < node.parent_node._data:
                    node.parent_node.left_node = node.right_node
                else:
                    node.parent_node.right_node = node.right_node
                node.right_node.parent_node = node.parent_node
                node.parent_node = None
                node.right_node = None
        # 左节点存在，右节点不存在
        elif node.left_node is not None and node.right_node is None:
            if node == self.root:
                self.root = node.left_node
                self.root.parent_node = None
                node.left_node = None
            else:
                if node._data < node.right_node._data:
                    node.parent.left_node = node.left_node
                else:
                    node.parent_node.right_node = node.left_node
                node.left_node.parent_node = node.parent_node
                node.parent_node = None
                node.left_node = None
        #左右节点都存在的情况
        else:
            min_node = node.right_node
            #找到右子树的最小值节点
            if min_node.left_node:
                min_node = min_node.left_node

            if node._data != min_node._data:
                node._data = min_node._data
                self._del(min_node)
            # 右子树的最小值节点与被删除节点的值相等，再次删除原节点
            else:
                self._del(min_node)
                self._del(node)



    def pre_order(self,root):
        """
        前序遍历
        :param root:
        :return:
        """
        if root is None:
            return
        print(root._data,end=",")
        self.pre_order(root.left_node)
        self.pre_order(root.right_node)

    def in_order(self,root):
        """
        中序遍历,顺序遍历出数据
        :param root:
        :return:
        """
        if root is None:
            return
        self.in_order(root.left_node)
        print(root._data, end=",")
        self.in_order(root.right_node)

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
        print(root._data, end=",")


if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()
    datas = [10,8,15,12,16,6,9,15,15]
    for i in datas:
        binary_search_tree.add(i)

    binary_search_tree.pre_order(binary_search_tree.root)
    print("")
    binary_search_tree.in_order(binary_search_tree.root)
    print("")
    binary_search_tree.post_order(binary_search_tree.root)
    print("")
    print(binary_search_tree.search(15))
    binary_search_tree.delete(15)
    binary_search_tree.in_order(binary_search_tree.root)
    print("")



