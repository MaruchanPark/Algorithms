'''
문제 - https://www.acmicpc.net/problem/9466

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
'''

import sys
sys.setrecursionlimit(100000)

T = int(input())

def dfs(x):
    global result
    visited[x] = True
    trace.append(x)

    x_ = s[x]
    if visited[x_] == True:
        if x_ in trace:
            result += trace[trace.index(x_):]
        return
    else:
        dfs(x_)

for i in range(T):
    N = int(input())
    s = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (N+1)
    result = []
    for i in range(1, N+1):

        if visited[i] == False:
            trace = []
            dfs(i)

    print(N - len(result))
