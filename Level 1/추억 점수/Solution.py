def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for i in photo:
        x = 0
        for n in name:
            if n in i :
                x += dic[n]
            else: pass
        answer.append(x)
    return answer