# -*- coding: utf8 -*-


#用列表实现队列


class QueueByList():
    """
    实现队列数据结构
    """
    def __init__(self,size):
        """
        初始化确定队列大小
        :param size:
        """
        self.queue = []
        self.size = size

    def __str__(self):
        return str(self.queue)

    def length(self):
        """
        队列大小
        :return:
        """
        return len(self.queue)

    def is_empty(self):
        """
        队列是否为空
        :return:
        """
        return self.length() == 0

    def is_full(self):
        """
        队列是否已满
        :return:
        """
        return self.length() == self.size

    def enqueue(self,data):
        """
        入队操作
        :param data:
        :return:
        """
        if not self.is_full():
            self.queue.append(data)
        else:
            raise Exception("queue is full")

    def dequeue(self):
        """
        出队操作
        :return:
        """
        if not self.is_empty():
            data = self.queue.pop(0)
            return data
        else:
            raise Exception("queue is empty")

    def clear(self):
        """
        清空队列
        :return:
        """
        self.queue = []


if __name__ == '__main__':
    queue = QueueByList(5)
    print (queue.is_empty())
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.__str__())
    print(queue.is_full())
    data = queue.dequeue()
    print(data)