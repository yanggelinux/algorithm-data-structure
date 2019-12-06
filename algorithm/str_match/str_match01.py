# -*- coding: utf8 -*-


def to_strs(str_list):
    res = ''.join([''.join(item) for item in str_list])
    return res


def find_str(m_str, p_str):
    m = len(m_str)
    n = len(m_str[0])

    k = len(p_str)
    p = len(p_str[0])
    p_res = to_strs(p_str)
    for i in range(m - k + 1):
        for j in range(n - p + 1):
            res_list = []
            for x in range(k):
                res_list.append([m_str[i+x][j], m_str[i+x][j + p - 1]])
            res = to_strs(res_list)
            if res == p_res:
                return True
    return False


if __name__ == '__main__':
    m_str = [
        ["d", "a", "b", "c"],
        ["e", "f", "a", "d"],
        ["c", "c", "a", "f"],
        ["d", "e", "f", "c"]
    ]
    p_str = [
        ["c", "a"],
        ["e", "f"],
    ]
    print(find_str(m_str, p_str))
