'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''

import math
M, N = map(int, input().split())

primes = [True] * (N + 1)
primes[1] = False

#2부터 N의 제곱근까지 나누어 떨어지는 수 제외
for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i] == True:
        #에라토스테네스의 체
        for j in range(i + i, N + 1, i):
            primes[j] = False

for i in range(M, N + 1):
    if primes[i] == True:
        print(i)
