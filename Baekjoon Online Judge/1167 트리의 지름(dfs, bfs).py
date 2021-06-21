'''
문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가
다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.
'''

#임의의 시작 기점으로부터 최대 가중치를 가진 노드는 지름을 이룰 수 있는 노드 중 하나이다.
#1. 임의의 노드에서 시작하여 DFS로 가장 멀리 있는 노드를 탐색
#2. 1에서 탐색한 노드에서 시작하여 가장 멀리 있는 노드를 탐색
#3. 2에서 탐색한 거리가 트리의 지름이 된다

import sys

V = int(input())
graph = [[] for _ in range(V + 1)]

for i in range(V):
    nums = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(nums) - 1, 2):
        graph[nums[0]].append([nums[j], nums[j + 1]])

max_ = [0, 0]
def dfs(node, length):

    if length > max_[0]:
        max_[0] = length
        max_[1] = node

    for line in graph[node]:
        if visited[line[0]] == False:

            visited[line[0]] = True
            dfs(line[0], length + line[1])

visited = [False] * (V + 1)
visited[1] = True
dfs(1,0)

visited = [False] * (V + 1)
visited[max_[1]] = True
dfs(max_[1], 0)

print(max_[0])
