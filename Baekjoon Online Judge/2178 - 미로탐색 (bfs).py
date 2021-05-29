import sys
from collections import deque

N, M = map(int,input().split())

map_ = []
for i in range(N):
    map_.append(sys.stdin.readline().rstrip())


queue = deque()
queue.append([0,0])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[0] * M for i in range(N)]
visited[0][0] = 1


while queue:
    x,y = queue.popleft()
    tmp = visited[y][x]

    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]

        if 0 <= x_ < M and 0 <= y_ < N and visited[y_][x_] == 0 and map_[y_][x_] == '1':
            queue.append([x_, y_])
            visited[y_][x_] += tmp + 1

print(visited[N-1][M-1])
