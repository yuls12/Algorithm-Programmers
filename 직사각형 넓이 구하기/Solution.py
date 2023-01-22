def solution(dots):
    dots.sort()
    x, y = dots[1][1] - dots[0][1], dots[2][0] - dots[0][0], 
    return x * y