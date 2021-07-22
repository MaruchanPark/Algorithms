'''
문제 https://www.acmicpc.net/problem/2206
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

# 벽을 부순 경우, 벽을 부수지 않은 경우에 대한 2xNxM 리스트에 거리를 기록하며 BFS 탐색을 한다.
# 벽을 부수지 않았을 때는 벽을 부수고 이동, 부수지 않고 이동하는 경우를 큐에 추가.
# 벽을 이미 부쉈을 때는 벽을 부수지 않고 이동하는 경우만 큐에 추가.
# 최종 위치에서 더 작은 거리가 정답이 된다. (0인 경우는 이동하지 못하는 경우이므로 제외)

from collections import deque

N, M = map(int, input().split())
map_ = []
for i in range(N):
    map_.append(input())

visited = [[[0] * M for _ in range(N)] for _ in range(2)]
queue = deque()
queue.append([0,0,0])
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    z,x,y = queue.popleft()

    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]

        if 0 <= x_ < N and 0 <= y_ < M:
            if visited[z][x_][y_] == 0:
                if map_[x_][y_] == '0':
                    visited[z][x_][y_] = visited[z][x][y] + 1
                    queue.append([z, x_, y_])

                if z == 0 and map_[x_][y_] == '1':
                    visited[1][x_][y_] = visited[z][x][y] + 1
                    queue.append([1, x_, y_])

sol_1 = visited[0][N-1][M-1]
sol_2 = visited[1][N-1][M-1]

if sol_1 == 0 and sol_2 == 0:
    print(-1)

elif sol_1 != 0 and sol_2 != 0:
    print(min(sol_1, sol_2))

else:
    print(max(sol_1, sol_2))
