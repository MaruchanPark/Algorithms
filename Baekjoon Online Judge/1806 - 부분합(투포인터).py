'''
문제 https://www.acmicpc.net/problem/1806
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
'''

# part_sums에 0부터 i까지의 합을 미리 구해서 연산을 줄인다
# 합을 미리 구해놓은 리스트 성분끼리 빼기 연산을 통해서, 연속된 성분들의 부분합을 구할 수 있다. (sum()보다 연산 횟수가 적다)

import sys

N, S = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))

part_sums = [0] * (N + 1)
for i in range(1, N + 1):
    part_sums[i] = nums[i-1] + part_sums[i-1]

start = 0
end = 1
min_ = N + 1
while start < N and end <= N:
    sum_ = part_sums[end] - part_sums[start]
    if sum_ < S:
        end += 1
    elif sum_ >= S:
        min_ = min(min_, end - start)
        start += 1

if min_ == N + 1:
    print(0)
else:
    print(min_)
