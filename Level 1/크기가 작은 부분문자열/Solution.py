def solution(t, p):
    answer = []
    for i in range(len(t) - len(p) +1):
        if int(t[i:i+len(p)]) <= int(p) :
            answer.append(int(t[i:i+len(p)]))
    return len(answer)