def solution(s):
    s_list = list(map(int, s.split(' ')))
    s_list.sort()
    return str(s_list[0]) + ' ' + str(s_list[-1])