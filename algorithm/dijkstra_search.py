# -*- coding: utf8 -*-




nodes = {
    "a":{"b":0.2,"c":0.3},
    "b":{"d":0.2,"f":0.3},
    "c":{"d":0.4,"e":0.1},
    "d":{"e":0.3},
    "e":{"f":0.2},
    "f":{}
}
finish = {}
mw = {}

def get_min_val(dicts={}):
    if dicts:
        val_list = []
        re_dicts = {}
        for k,v in dicts.items():
            val_list.append(v)
            re_dicts[v] = k
        min_val = min(val_list)
        min_key = re_dicts[min_val]
        return min_key


def dijkstra_search():
    mw["a"] = 0
    finish["a"] = 0
    queue = []
    queue.append(nodes["a"])
    while queue:
        node = queue.pop(0)
        min_key = get_min_val(node)
        if min_key is not None:
            finish[min_key] = node[min_key]
        print(finish)
        for nd,val in node.items():
            if finish.get(nd) is not None:
                queue.append(nodes[nd])




if __name__ == '__main__':
    dijkstra_search()