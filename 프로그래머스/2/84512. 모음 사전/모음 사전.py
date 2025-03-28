from itertools import *
def solution(word):
    data = []
    sorted_list = []
    a_list = []
    e_list = []
    i_list = []
    o_list = []
    u_list = []
    for i in range(1, 6):
        tmps = set(list(map(''.join,product("AEIOU", repeat=i))))
        data.extend(tmps)
    for i in data:
        if i.startswith('A'):
            a_list.append(i)
        elif i.startswith('E'):
            e_list.append(i)
        elif i.startswith('I'):
            i_list.append(i)
        elif i.startswith('O'):
            o_list.append(i)
        else:
            u_list.append(i)
    sorted_list.extend(sorted(a_list))
    sorted_list.extend(sorted(e_list))
    sorted_list.extend(sorted(i_list))
    sorted_list.extend(sorted(o_list))
    sorted_list.extend(sorted(u_list))
    return sorted_list.index(word) + 1