'''
문제 - https://www.acmicpc.net/problem/2751
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# 값의 범위가 크지 않으므로 list로 등장 횟수를 카운트해서 순서대로 출력한다.

import sys

N = int(input())

abs_max = 1000000
nums = [0] * (abs_max * 2 + 1)

for i in range(N):
    num = int(sys.stdin.readline())

    nums[num + abs_max] += 1

for i in range(abs_max * 2 + 1):
    for j in range(nums[i]):
        print(i - abs_max)
