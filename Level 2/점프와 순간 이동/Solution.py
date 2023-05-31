def solution(n):
    ans = 0
    while n > 0 :
        x, y = divmod(n,2)
        n = x
        if y != 0:
            ans += 1
    return ans