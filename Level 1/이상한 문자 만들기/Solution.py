def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s :
        for k in range(len(i)) :
            if k % 2 == 0 :
                answer += i[k].upper()
            else :
                answer += i[k].lower()
        answer += ' '
    
    return answer[:-1]