def solution(lines):
    answer = 0
    table = [0 for _ in range(200)]
    for line in lines:
        for i in range(line[0], line[1]):
            table[i + 100] += 1
    answer += table.count(2)
    answer += table.count(3)
    return answer
