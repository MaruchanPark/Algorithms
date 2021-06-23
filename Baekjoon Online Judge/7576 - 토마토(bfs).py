'''
문제 https://www.acmicpc.net/problem/7576
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지,
그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는
상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''

# 상하좌우 BFS로 탐색하면서 이전 방문횟수에 1을 더해나간다.

from collections import deque
import sys

M, N = map(int, input().split())

map_ = []
for i in range(N):
    map_.append(list(map(int, sys.stdin.readline().split())))

queue = deque()
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

condition = 0
for i in range(N):
    if 0 in map_[i]:
        condition = 1

for i in range(N):
    for j in range(M):
        if map_[i][j] == 1:
            queue.append([i, j])

while queue:
    row, col = queue.popleft()

    for i in range(4):
        row_ = row + d_row[i]
        col_ = col + d_col[i]

        if 0 <= row_ < N and 0 <= col_ < M and map_[row_][col_] == 0:
            map_[row_][col_] = map_[row][col] + 1

            queue.append([row_, col_])

for i in range(N):
    if 0 in map_[i]:
        condition = -1

if condition == 0 or condition == -1:
    print(condition)
else:
    max_ = 0
    for i in map_:
        max_ = max(max_,max(i))
    print(max_ - 1)
