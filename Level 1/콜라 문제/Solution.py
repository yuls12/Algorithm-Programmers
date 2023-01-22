def solution(a, b, n):
    c = 0
    while n >= a:
        x, y = divmod(n, a)
        c += x * b
        r = y
        n = x * b + y
    return c