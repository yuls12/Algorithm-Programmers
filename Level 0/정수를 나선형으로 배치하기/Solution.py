def solution(n):
    answer = [[0] * n for _ in range(n)]
    locs = 1
    cnt = 1
    row, col = 0, -1

    while n > 0:
        for i in range(n):
            col += locs
            answer[row][col] = cnt
            cnt += 1
        n -= 1
        for i in range(n):
            row += locs
            answer[row][col] = cnt
            cnt += 1

        locs *= -1

    return answer
