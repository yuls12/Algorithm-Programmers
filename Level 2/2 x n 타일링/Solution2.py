def solution(n):
    a, b = 1, 2
    for i in range(1, n):
        a, b = b , a + b
    return a % 1000000007