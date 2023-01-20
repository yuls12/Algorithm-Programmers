def solution(s):
    dic = {}
    for i in s:
        if i not in dic.keys() :
            dic[i]  = 0
        else : 
            dic[i]  += 1
    return ''.join(sorted([k for k, v in dic.items() if v == 0]))