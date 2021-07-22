'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''

# 모든 이동 방법에 대해 처음 방문하는 곳만 BFS로 탐색할 때 가장 먼저 도착한 경로가 정답이다.

from collections import deque

N, K = map(int, input().split())

visited = [0] * (100001)
queue = deque()

queue.append([N, 0])
visited[N] = -1

while queue:
    visit = queue.popleft()
    n = visit[0]
    if n == K:
        print(visit[1])
        break

    if 0 <= n-1 and visited[n - 1] == False:
        visited[n - 1] = True
        queue.append([n-1, visit[1] + 1])

    if n+1 <= 100000 and visited[n + 1] == False:
        visited[n + 1] = True
        queue.append([n+1, visit[1] + 1])

    if n*2 <= 100000 and visited[n*2] == False:
        visited[n*2] = True
        queue.append([n*2, visit[1] + 1])
