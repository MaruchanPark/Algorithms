'''
문제 https://www.acmicpc.net/problem/2573

입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.
'''

# BFS로 일년이 지났을 때의 빙산을 계산
# DFS로 덩어리의 갯수를 

import sys
from collections import deque

N, M = map(int, input().split())
map_ = []
for i in range(N):
    map_.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def one_year(n, m):

    temp = [[0] * M for _ in range(N)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if map_[i][j] != 0:
                for k in range(4):
                    x_ = i + dx[k]
                    y_ = j + dy[k]

                    if 0 <= x_ < N and 0 <= y_ < M and map_[x_][y_] == 0:
                        temp[i][j] -= 1

    for i in range(n):
        for j in range(m):
            map_[i][j] = max(map_[i][j] + temp[i][j], 0)

    check = 0
    for i in range(n):
        check += sum(map_[i])

    return check

def count_chunk(n, m):
    visited = [[False] * M for _ in range(N)]
    stack = []
    n_chunk = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if map_[i][j] != 0 and visited[i][j] == False:
                n_chunk += 1
                stack.append([i,j])
                visited[i][j] = n_chunk

                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        x_ = x + dx[k]
                        y_ = y + dy[k]

                        if map_[x_][y_] != 0 and visited[x_][y_] == False:
                            visited[x_][y_] = n_chunk
                            stack.append([x_, y_])
    return n_chunk

answer = 0
year = 0
while True:
    sum_ = one_year(N, M)
    chunks = count_chunk(N,M)
    year += 1

    if sum_ == 0:
        print(0)
        break
    if chunks > 1:
        print(year)
        break
