def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))