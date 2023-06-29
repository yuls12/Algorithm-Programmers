import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            cnt += 1
        else:
            return -1
    return cnt