# -*- coding: utf8 -*-


"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self._data) > 0:
            self._data.pop()
        else:
            raise Exception("stack is empty")
    def top(self):
        """
        :rtype: int
        """
        if len(self._data) > 0:
            return self._data[-1]
        else:
            raise Exception("stack is empty")

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._data) >0:
            return min(self._data)
        else:
            raise Exception("stack is empty")


class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min_data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._data.append(x)
        if len(self._min_data) > 0:
            old_min_val = self._min_data[-1]
            if x <= old_min_val:
                self._min_data.append(x)
        else:
            self._min_data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self._data) > 0:
            p = self._data.pop()
            if len(self._min_data) > 0:
                min_val = self._min_data[-1]
                if p == min_val:
                    self._min_data.pop()
        else:
            raise Exception("stack is empty")
    def top(self):
        """
        :rtype: int
        """
        if len(self._data) > 0:
            return self._data[-1]
        else:
            raise Exception("stack is empty")

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._min_data) >0:
            return self._min_data[-1]
        else:
            raise Exception("stack is empty")