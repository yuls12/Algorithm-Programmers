from collections import deque, defaultdict

def solution(n, edge):
    distance = [0] * (n + 1)
    graph = defaultdict(list)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque()
    q.append(1)

    while q:
        recent = q.popleft()
        dist = distance[recent]

        for neighbor in graph[recent]:
            if neighbor != 1 and distance[neighbor] == 0:
                q.append(neighbor)
                distance[neighbor] = dist + 1

    return distance.count(max(distance))