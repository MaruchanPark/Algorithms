'''
문제 https://www.acmicpc.net/problem/2805

입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다.
높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
'''

# 자른 나무의 길이가 "최소"가 되게 하는 나무의 길이를 이분 탐색으로 찾는다.
# 최대 길이를 찾는 이분 탐색과 조건을 반대로 해야 함.

import sys

N, M = map(int,input().split())

tree=list(map(int, sys.stdin.readline().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    cut = 0
    for i in range(N):
        cut += max(tree[i] - mid, 0)

    if cut >= M:
        start = mid + 1

    elif cut < M:
        end = mid - 1

print(end)
