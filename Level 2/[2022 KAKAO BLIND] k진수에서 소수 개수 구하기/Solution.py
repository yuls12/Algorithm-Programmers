def solution(n, k):
    word = ""
    while n:  # 숫자를 k진법으로 변환
        word = str(n % k) + word
        n = n // k

    word = word.split("0")
    count = 0
    for w in word:
        if len(w) == 0 or int(w) < 2:
            continue
        sosu = True
        for i in range(2, int(int(w)**0.5) + 1):
            if int(w) % i == 0:
                sosu = False
                break
        if sosu:
            count += 1

    return count