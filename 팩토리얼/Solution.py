def factorial(k):
    if k > 1 :
        return k * factorial(k-1)
    else:
        return 1

def solution(n):
    fact = [factorial(i) for i in range(1,11)]
    answer = [i for i in fact if n >= i]
    return len(answer)