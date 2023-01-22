def solution(M, N):
    width, height = min(M,N), max(M,N)
    w_count = width - 1
    h_count = (height - 1) * width
    answer = w_count + h_count
    return answer