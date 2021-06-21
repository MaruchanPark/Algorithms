# 재귀 DFS로 구현하면 recursionlimit 설정이 필요하다.
# BFS 풀이도 추가할 것.

import sys
sys.setrecursionlimit(1000000)
N = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    node_a, node_b = map(int, sys.stdin.readline().split())
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

visited = [False] * (N + 1)
parents = []
def dfs(start):
    visited[start] = True

    for node in graph[start]:
        if visited[node] == False:
            parents.append([node, start])
            dfs(node)

dfs(1)

parents.sort(key = lambda x: (x[0]))

for i in parents:
    print(i[1])
