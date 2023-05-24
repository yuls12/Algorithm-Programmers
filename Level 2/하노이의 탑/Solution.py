def hanoi(From, To, Sub, n):
    global answer
    if n == 1:
        answer.append([From, To])
    else:
        hanoi(From, Sub, To, n-1)
        answer.append([From, To])
        hanoi(Sub, To, From, n-1)


def solution(n):
    global answer
    answer = []
    hanoi(1, 3, 2, n)
    return answer