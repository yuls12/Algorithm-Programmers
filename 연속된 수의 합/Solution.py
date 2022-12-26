def solution(num, total):
    q, r = divmod(total, num)
    if r == 0:
        answer = [i for i in range(q - (num // 2), q + (num // 2) + 1)]
    else:
        answer = [i for i in range(q - (num - 1) // 2, q + (num + 1) // 2 + 1)]
    return answer