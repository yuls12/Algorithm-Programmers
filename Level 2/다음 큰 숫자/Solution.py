def solution(n, count=0):
    return n if bin(n).count("1") is count else solution(n+1, bin(n).count("1") if count is 0 else count)
