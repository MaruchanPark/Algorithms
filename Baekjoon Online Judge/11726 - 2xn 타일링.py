'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''

# 직사각형을 채우는 방법의 수는 피보나치 수열을 이룬다.

n = int(input())

A = [0] * n

A[0] = 1
if n > 1:
    A[1] = 2

for i in range(2, n):
    A[i] = A[i-1] + A[i-2]

print(A[-1] % 10007)
