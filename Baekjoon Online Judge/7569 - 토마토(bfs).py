'''
문제 - https://www.acmicpc.net/problem/7569

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

# x, y, z 3차원 여섯 방향으로 bfs 탐색.

from collections import deque

M, N, H = map(int, input().split())

map_ = []

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,input().split())))
    map_.append(temp)

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

queue = deque()

rip = 1
for i in range(H):
    for j in range(N):
        if 0 in map_[i][j]:
            rip = 0
        for k in range(M):
            if map_[i][j][k] == 1:
                queue.append([k, j, i])

if rip == 1:
    print(0)

else:
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            x_ = x + dx[i]
            y_ = y + dy[i]
            z_ = z + dz[i]

            if 0 <= x_ < M and 0 <= y_ <N and 0 <= z_ < H and map_[z_][y_][x_] == 0:
                map_[z_][y_][x_] = map_[z][y][x] + 1
                queue.append([x_, y_, z_])

    days = 0
    rip = 1
    for i in range(H):
        for j in range(N):
            if 0 in map_[i][j]:
                rip = 0
            days = max(days, max(map_[i][j]))

    if rip == 1:
        print(days - 1)
    else:
        print(-1)
