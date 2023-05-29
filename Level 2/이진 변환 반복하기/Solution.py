def solution(s):
    zero = 0
    cnt = 0
    while int(s) > 1 :
        s = sorted(s)
        zero += s.count('0')
        s = ''.join(s[s.index('1'):])
        s = bin(int(len(s)))[2:]
        cnt += 1

        if s == '1':
            break
    return [cnt, zero]