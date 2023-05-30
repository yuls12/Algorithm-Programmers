def solution(n):
    count = 0
    for i in range(1, n + 1):
        add_num = 0
        for k in range(i, n + 1):
            add_num += k
            if add_num == n:
                count += 1
                break
            if add_num > n:
                break
    return count
