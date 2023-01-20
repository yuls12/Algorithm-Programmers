def solution(bin1, bin2):
    a, b = int(bin1, 2), int(bin2, 2)
    x = bin(a + b)[2:]
    return x