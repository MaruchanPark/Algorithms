'''
문제  https://www.acmicpc.net/problem/2667
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고,
단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''

#지도의 값이 1이면 BFS 탐색으로 연결된 모든 집을 단지수+1 의 값으로 할당. (첫 번재 집의 중복 탐색을 막기 위해 단지수+1 로 할당한다.)
#BFS에 탐색된 집의 갯수를 세서 출력

import sys
from collections import deque

N = int(input())
map_ = []

for i in range(N):
    map_.append(list(map(int,list(input().strip()))))

dv = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]

comp = 1

def bfs(row, column, num):
    queue = deque()
    queue.append([row, column])
    map_[row][column] = num
    cnt = 1

    while queue:
        v, h = queue.popleft()

        for i in range(4):
            v_ = v + dv[i]
            h_ = h + dh[i]

            if 0 <= v_ < N and 0 <= h_ < N and map_[v_][h_] == 1:
                queue.append([v_, h_])
                map_[v_][h_] = num
                cnt += 1
    return cnt

comps = []
for i in range(N):
    for j in range(N):
        if map_[i][j] == 1:
            comp += 1
            comps.append(bfs(i, j, comp))

print(comp - 1)
comps.sort()
for i in comps:
    print(i)
