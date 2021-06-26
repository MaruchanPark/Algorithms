'''
문제 https://www.acmicpc.net/problem/11725
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

# 재귀 DFS로 구현하면 recursionlimit 설정이 필요하다.
# while, stack을 이용해서 DFS 구현 시 런타임에러 발생하지 않음.

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

    
# BFS 풀이, DFS 보다 빠름
# parents 리스트 정렬하는 부분이 DFS 코드와 다른 점인데, 속도의 차이가 어디서 오는지 확인해볼 필요 있음

import sys
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    node_1, node_2 = map(int, sys.stdin.readline().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

parents = [0] * (n + 1)
parents[1] = 1
queue = deque()
queue.append(1)

while queue:
    visit = queue.popleft()

    for node in graph[visit]:
        if parents[node] == 0:
            parents[node] = visit
            queue.append(node)

for i in range(2, n + 1):
    print(parents[i])
