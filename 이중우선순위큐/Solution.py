from collections import deque
def solution(operations):
    de = deque([])
    for i in operations:
        if i[0] == 'I':
            de.append(int(i[2:]))
        elif i == 'D -1':
            if len(de) > 0 :
                de.remove(min(de))
        elif i == 'D 1':
            if len(de) > 0 :
                de.remove(max(de))

    if len(de) == 0:
        return [0,0]
    else :
        return [max(de), min(de)]