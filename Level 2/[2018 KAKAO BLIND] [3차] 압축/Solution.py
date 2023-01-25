def solution(msg):
    voca = []
    for i in range(97, 123):
        voca.append(chr(i).upper())

    dic = {}
    for i, v in enumerate(voca, start=1):
        dic[v] = i

    answer = []
    idx = 27
    start, end = 0, 1

    while end < len(msg) + 1:
        s = msg[start:end]
        if s in dic:
            end += 1
        else:
            answer.append(dic[s[:-1]])
            dic[s] = idx 
            idx += 1
            start = end -1
    answer.append(dic[s])
    return answer