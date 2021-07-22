'''
문제 - https://www.acmicpc.net/problem/1707
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와
간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

출력
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
'''

# 연결된 정점을 방문하며, 1과 -1로 표시한다.
# 이전 정점에 -1을 곱한 값으로 표시를 하며, 인접 정점의 값이 같으면 NO를 출력한다.
# 분리되어 있는 그래프의 경우도 상정해서 방문하지 않은 모든 정점을 bfs로 탐색
# bfs로 처음 방문하는 값은 1로 한다. (이전 bfs 탐색에서 방문하지 않은 분리된 정점들이므로 1, -1중 어떤 값을 해도 상관 없음)

from collections import deque
import sys

K = int(input())

def bfs(start):

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        visit = queue.popleft()

        for visit_ in graph[visit]:
            if visited[visit_] == 0:
                visited[visit_] = visited[visit] * -1
                queue.append(visit_)

            elif visited[visit_] == visited[visit]:
                return False

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for __ in range(E):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    visited = [0] * (V + 1)

    for i in range(1, V+1):
        if visited[i] == 0:
            isTrue = bfs(i)

        if isTrue == False:
            print('NO')
            break
    if isTrue == None:
        print('YES')
