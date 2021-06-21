#한번 더 풀어볼 것. 예외를 고려하지 못함

import sys
from collections import deque

def bfs(start):
    queue = deque()

    queue.append(start)
    visited[start] = 1

    while queue:
        visit = queue.popleft()

        for node in graph[visit]:
            if visited[node] == 0:
                visited[node] = visited[visit] * (-1)
                queue.append(node)

            elif visited[node] == visited[visit]:
                return False
    return True

K = int(input())
for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for j in range(E):
        node_a, node_b = map(int, sys.stdin.readline().split())
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    visited = [0] * (V + 1)
    for j in range(1, V + 1):
        if visited[j] == 0:
            isTrue = bfs(j)

            if not isTrue:
                break

    if not isTrue:
        print('NO')
    else:
        print('YES')
