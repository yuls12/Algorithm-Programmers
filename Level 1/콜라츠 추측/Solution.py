def solution(num):
    answer = 0
    if num == 1:
        return 0
    while num > 1: 
        num = num/2 if num % 2 == 0 else (num*3)+1 
        answer += 1 
        
    return answer if answer < 500 else -1