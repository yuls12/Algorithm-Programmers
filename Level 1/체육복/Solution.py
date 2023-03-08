def solution(n, lost, reserve):
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)
    
    answer = n - len(lost_del)
    for i in reserve_del: 
        if i-1 in lost_del: 
            answer += 1
            lost_del.remove(i-1) 
        elif i+1 in lost_del: 
            answer += 1
            lost_del.remove(i+1)

    return answer