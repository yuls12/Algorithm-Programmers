# 이분탐색법
## 중간값으로 check하며 범위를 좁혀나가는 방법
def solution(n, times):
    answer = 0
    left, right = min(times), max(times) * n

    while left <= right:
        mid = (left + right) // 2
        check = 0
        for i in times:
            check += mid // i
            if check >= n:
                break
        if check >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer