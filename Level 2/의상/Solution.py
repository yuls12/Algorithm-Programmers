def solution(clothes):
    dict = {}
    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1
        else:
            dict[i[1]] = 1

    cnt = 1
    for i in dict.values():
        cnt *= (i + 1)
    return cnt - 1
