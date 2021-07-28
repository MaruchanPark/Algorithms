'''
문제 - https://www.acmicpc.net/problem/10451

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
'''

# 탐색하지 않은 노드를 dfs로 탐색한다.
# dfs는 연결된 모든 노드를 방문하므로 방문 횟수가 정답이 된다.

import sys
sys.setrecursionlimit(100000)

T = int(input())

def dfs(x):
    if visited[s[x]] == False:
        visited[s[x]] = True
        dfs(s[x])

for i in range(T):
    N = int(input())
    s = list(map(int, sys.stdin.readline().split()))
    s.insert(0, 0)

    cnt = 0
    visited = [False] * (N + 1)

    for i in range(1, len(s)):
        if visited[s[i]] == False:
            cnt += 1
            dfs(s[i])
            
    print(cnt)
