def solution(prices):

    sec = [0] * len(prices)
    for i in range(len(prices)-1):
        for k in range(i, len(prices)-1):
            if prices[i] >prices[k]:
                break
            else:
                sec[i] +=1
    return sec