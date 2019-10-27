# -*- coding: utf8 -*-

'''
#递归模版
def recursion(level, param1, param2, ...):
    # recursion terminator 终止条件
    if level > MAX_LEVEL:
	   process_result
	   return

    # process logic in current level 逻辑层
    process(level, data...)

    # drill down
    recursion(level + 1, p1, ...)

    # reverse the current level status if needed


#分治模版
def divide_and_conquer(datas, paras):
    if exit_condition(datas): #终止条件
        return
    subData = split_data(datas)  #问题可被分解为不同的子问题
    result1 = divide_and_conquer(subdata[0], paras)
    result2 = divide_and_conquer(subdata[1], paras)
    result3 = divide_and_conquer(subdata[2], paras)
    ...
    result = mergy_data(result1, result2. result3...) #问题的结果可被还原为整体
    return result

#回溯模版
def backtracking(level, paras):
    if exist_condition(level):
        return
    state = keepsate(level)  #保存当前状态
    backtracking(level+1, paras):
    reverseState(level, state) #恢复当前状态

'''