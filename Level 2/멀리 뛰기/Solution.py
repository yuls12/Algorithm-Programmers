# DP 문제 
## 방법을 나타낼 수 있는 구칙성이 존재함 (d_i = d_(i-1) + d_(i-2))
def solution(n):
    if n < 3:
        return n
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n] % 1234567