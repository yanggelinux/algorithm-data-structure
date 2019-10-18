# -*- coding: utf8 -*-


#列表实现栈


class StackByList(object):

    def __init__(self):
        """
        初始化stack
        """
        self.stack = []


    def push(self,data):
        """
        入栈操作,添加元素
        :param data:
        :return:
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈操作，删除元素并返回
        :return:
        """
        if not self.is_empty():
            data = self.stack.pop()
            return data
        else:
            raise Exception("stack is empty")

    def peek(self):
        """
        获取栈顶元素
        :return:
        """
        data = self.stack[-1]
        return data
    def clear(self):
        """
        清空栈
        :return:
        """
        self.stack = []

    def length(self):
        """
        栈长度
        :return:
        """
        return len(self.stack)

    def is_empty(self):
        """
        栈是否为空
        :return:
        """
        return self.length() == 0

    def travel(self):
        """
        遍历栈
        :return:
        """
        print("[",end=" ")
        for i in self.stack:
            print(i,end=" ")
        print("]")

if __name__ == '__main__':
    stack = StackByList()
    stack.pop()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)

    data = stack.pop()
    print(data)
    stack.travel()
    print(stack.length())

