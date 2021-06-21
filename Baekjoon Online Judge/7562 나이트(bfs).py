'''
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다.
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''

#자리마다 이동횟수를 더해주면서 BFS 탐색, 목적지에 도착하면 중단하고 출력

import sys
from collections import deque

def bfs(s_x, s_y, e_x, e_y, width):
    visited = [[0] * width for i in range(width)]
    queue = deque()
    queue.append([s_x, s_y])

    visited[s_y][s_x] = 1

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while queue:
        x, y = queue.popleft()

        if x == e_x and y == e_y:
            return visited[e_y][e_x]


        for i in range(8):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if 0 <= x_ < width and 0 <= y_ < width and visited[y_][x_] == 0:
                visited[y_][x_] = visited[y][x] + 1
                queue.append([x_, y_])

N = int(input())

for i in range(N):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(bfs(sx, sy, ex, ey, l) - 1)
