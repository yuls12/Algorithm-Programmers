def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        cnt = []
        x = discount[i:i+10]
        for j in want:
            cnt.append(x.count(j))
        if number == cnt:
            answer += 1
    return answer