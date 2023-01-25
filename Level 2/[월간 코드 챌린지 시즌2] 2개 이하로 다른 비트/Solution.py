def solution(numbers):
    answer = []
    for n in numbers:
        t = list('0' + bin(n)[2:])
        idx = ''.join(t).rfind('0')
        t[idx] = '1'
        
        if n % 2 == 1:
            t[idx+1] = '0'
        answer.append(int(''.join(t), 2))
    return answer