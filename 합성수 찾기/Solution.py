def solution(n):
    answer = 0
    cnt = []
    for i in range(2,n+1):
        for k in range(1, i+1):
            if i % k == 0 :
                cnt.append(i)
        if cnt.count(i) >= 3:
            answer += 1
    return answer