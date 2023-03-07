from collections import deque

def solution(cards1, cards2, goal):
    card1 = deque(cards1)
    card2 = deque(cards2)
    for i in goal:
        if len(card1) > 0 and i in card1[0]:
            card1.popleft()
        elif len(card2) > 0 and i in card2[0]:
            card2.popleft()
        else:
            return 'No'
    return 'Yes'