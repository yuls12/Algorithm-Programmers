def yaksu(k):
    cnt = 0
    for i in range(1, int(k **(1/2))+1):
        if k % i == 0:
            if i == k//i:
                cnt += 1
            else:
                cnt += 2 
    return cnt

def solution(number, limit, power):
    weap = [yaksu(i) for i in range(1, number+1)]
    answer = 0 
    for i in weap:
        if i <= limit:
            answer += i
        else :
            answer += power
    return answer