import math


def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    k -= 1

    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i - 1))
        answer.append(numbers.pop(div))

    return answer
