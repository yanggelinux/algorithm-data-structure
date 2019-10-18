# -*- coding: utf8 -*-


#利用栈匹配括号

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
        data = self.stack.pop()
        return data

    def peek(self):
        """
        获取栈顶元素
        :return:
        """
        data = self.stack[-1]
        return data

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



def match_brackets(stack,string):
    """
    利用栈做括号的匹配
    :param stack:
    :param string:
    :return:
    """
    match_flag = False
    #括号对应map
    bracket_map = {"(":")","[":"]","{":"}"}
    for s in string:
        #如果字符是左括号，入栈
        if s in ["(","[","{"]:
            stack.push(s)
            #匹配标示为True
            match_flag = True
        #如果字符是右括号，出栈，并对比括号是否匹配
        if s in [")","]","}"]:
            p =stack.pop()
            #括号不匹配返回False
            if bracket_map[p] != s:
                return False
            else:
                #括号匹配匹配标示为重置False
                match_flag = False
    else:
        #如果字符串都遍历完，还有每匹配的括号，返回False
        if match_flag:
            return False
    return True


def forward_and_backward(stacka,stackb):
    """
    利用两个栈模拟浏览器前进后退的功能
    :param stacka: 存放前进的页面
    :param stackb: 存放后退的页面
    :return:
    """
    pass


class Browser(object):
    """
    利用两个栈模拟浏览器前进后退的功能
    """
    def __init__(self):
        self.f_stack = StackByList()
        self.b_stack = StackByList()

    def click_link(self,page):
        """
        点击链接跳转页面
        :param page:
        :return:
        """
        #前进页面栈添加页面
        print("点击-当前页面:", page)
        self.f_stack.push(page)

    def click_backward(self):
        """
        点击后退按钮
        :return:
        """
        #如果前进栈里有数据
        if not self.f_stack.is_empty():
            #从前进栈取出数据
            page = self.f_stack.pop()
            #放到后退栈中
            print("后退-当前页面:",page)
            self.b_stack.push(page)
        else:
            print("forward stack is empty")

    def click_forward(self):
        """
        点击前进按钮
        :return:
        """
        #如果后退栈中有数据
        if not self.b_stack.is_empty():
            #从后退栈中取数据放入前进栈
            page = self.b_stack.pop()
            print("前进-当前页面:", page)
            self.f_stack.push(page)
        else:
            print("backward stack is empty")




if __name__ == '__main__':
    stack = StackByList()
    string = "我最爱的(人)[]是?"
    res = match_brackets(stack, string)
    print("是否匹配成功:",res)
    f_stack = StackByList()
    b_stack = StackByList()
    browser = Browser()
    browser.click_link("page1")
    browser.click_link("page2")
    browser.click_link("page3")
    browser.click_backward()
    browser.click_backward()
    browser.click_forward()

