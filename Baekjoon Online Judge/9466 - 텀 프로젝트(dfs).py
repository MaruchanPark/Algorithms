'''
문제 - https://www.acmicpc.net/problem/9466

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
'''

# 순환 사이클이 있는지 dfs로 탐색
# 노드간의 연결은 일대일 대응이므로, 한 노드에 여러 노드가 방문하는 경우는 고려하지 않아도 됨.
# 순환 사이클이 있으면 dfs 함수 내에서 visited[방문] == True가 발생함
# 방문 경로들을 trace에 저장하고, 순환 사이클을 발견한 성분부터 끝까지가 순환사이클의 멤버가 됨

import sys
sys.setrecursionlimit(1000000)

T = int(input())

def dfs(start):
    global n_student
    if visited[nums[start]]:
        if nums[start] in trace:
            idx = trace.index(nums[start])
            n_student += len(trace[idx:])
            return

    elif not visited[nums[start]]:
        visited[nums[start]] = True
        trace.append(nums[start])
        dfs(nums[start])

for i in range(T):
    n = int(input())

    nums = list(map(int, sys.stdin.readline().split()))
    nums.insert(0,0)
    visited = [False] * (n + 1)
    n_student = 0

    for j in range(1,n+1):
        if not visited[j]:
            trace = [j]
            visited[j] = True
            dfs(j)
    print(n - n_student)
